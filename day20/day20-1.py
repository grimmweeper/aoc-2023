from collections import deque as queue

file_path = 'day20.txt'

class Signal:
    def __init__(self, _source, _destination, _pulse) -> None:
        self.source = _source
        self.destination = _destination
        self.pulse = _pulse
    
    def __str__(self) -> str:
        return "Source: {0}, Destination: {1}, Pulse: {2}".format(self.source, self.destination, self.pulse)


def prepareSignal(file):
    signalMap = {}
    moduleType = {}
    moduleStatus = {}
    for line in file:
        rawMapping = line.strip().split("->")
        rawInput = rawMapping[0].strip()
        rawOutput = rawMapping[1].strip()
        if (rawInput == "broadcaster"):
            broadcaster = [output.strip() for output in rawOutput.split(',')]
            moduleStatus = updateModuleStatus("broadcaster", broadcaster, moduleStatus)
        else:
            signalMap[rawInput[1:]] = [output.strip() for output in rawOutput.split(',')]
            moduleType[rawInput[1:]] = rawInput[0]
            moduleStatus = updateModuleStatus(rawInput[1:], signalMap[rawInput[1:]], moduleStatus)
        

    return broadcaster, signalMap, moduleType, moduleStatus

def updateModuleStatus(input, outputArray, moduleStatus):
    for output in outputArray:
        if (output not in moduleStatus):
            moduleStatus[output] = ["off", {input: "low"}]
        else:
            if (input not in moduleStatus[output][1]):
                newConjunctionStatus = {input: "low"}
                moduleStatus[output][1] = {**moduleStatus[output][1], **newConjunctionStatus}
    return moduleStatus

def pressSignalButton(signalMap, moduleType, moduleStatus):
    signalQueue = queue()
    for output in broadcaster:
        signal = Signal("broadcaster", output, "low")
        signalQueue.append(signal)

    lowPulse = 1
    highPulse = 0
    while(len(signalQueue) > 0):
        signal: Signal = signalQueue.popleft()
        # print(signal)
        if (signal.pulse == "low"):
            lowPulse += 1
        elif (signal.pulse == "high"):
            highPulse += 1

        if (signal.destination not in signalMap):
            continue


        destModule = moduleType[signal.destination]
        if (destModule == "%"):
            if (signal.pulse == "low"):
                destStatus = moduleStatus[signal.destination]
                if (destStatus[0] == "off"):
                    moduleStatus[signal.destination][0] = "on"
                    newPulse = "high"
                elif (destStatus[0] == "on"):
                    moduleStatus[signal.destination][0] = "off"
                    newPulse = "low"
                for dest in signalMap[signal.destination]:
                    newSignal = Signal(signal.destination, dest, newPulse)
                    signalQueue.append(newSignal)

        elif (destModule == "&"):
            moduleStatus[signal.destination][1][signal.source] = signal.pulse
            allInputHigh = all(pulse == "high" for pulse in moduleStatus[signal.destination][1].values())
            if (allInputHigh):
                newPulse = "low"
            else:
                newPulse = "high"
            for dest in signalMap[signal.destination]:
                newSignal = Signal(signal.destination, dest, newPulse)
                signalQueue.append(newSignal)

    return moduleStatus, lowPulse, highPulse
with open(file_path, 'r') as file:

    totalLowPulse = 0
    totalHighPulse = 0

    # broadcaster = ['a', 'b', 'c']
    # signalMap = {"a" : ["b"], "b": ["c"], "c": ["inv"], "inv": ["a"]}
    # moduleType = {"a": "%", "b": "%", "c": "%", "inv": "&"}
    # moduleStatus = {'a': ['off', {'broadcaster': 'low', 'inv': 'low'}], 'b': ['off', {'broadcaster': 'low', 'a': 'low'}], 'c': ['off', {'broadcaster': 'low', 'b': 'low'}], 'inv': ['off', {'c': 'low'}]}
    broadcaster, signalMap, moduleType, moduleStatus = prepareSignal(file)

    for i in range(1000):
        moduleStatus, lowPulse, highPulse = pressSignalButton(signalMap, moduleType, moduleStatus)
        totalLowPulse += lowPulse
        totalHighPulse += highPulse

    print(totalHighPulse * totalLowPulse)

