from collections import deque as queue
from math import lcm

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

    lastPdPulse = "low"
    lastBpPulse = "low"
    lastXcPulse = "low"
    lastThPulse = "low"

    while(len(signalQueue) > 0):
        signal: Signal = signalQueue.popleft()

        if (signal.destination == "zh"):
            if (signal.source == "pd"):
                if (signal.pulse == "high"):
                    lastPdPulse = "high"

            elif (signal.source == "bp"):
                if (signal.pulse == "high"):
                    lastBpPulse = "high"


            elif (signal.source == "xc"):
                if (signal.pulse == "high"):
                    lastXcPulse = "high"

            
            elif (signal.source == "th"):
                if (signal.pulse == "high"):
                    lastThPulse = "high"

            

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

    return moduleStatus, lastPdPulse, lastBpPulse, lastXcPulse, lastThPulse


with open(file_path, 'r') as file:

    buttonPressed = 0

    pdCycle = 0
    bpCycle = 0
    xcCycle = 0
    thCycle = 0

    # broadcaster = ['a', 'b', 'c']
    # signalMap = {"a" : ["b"], "b": ["c"], "c": ["inv"], "inv": ["a"]}
    # moduleType = {"a": "%", "b": "%", "c": "%", "inv": "&"}
    # moduleStatus = {'a': ['off', {'broadcaster': 'low', 'inv': 'low'}], 'b': ['off', {'broadcaster': 'low', 'a': 'low'}], 'c': ['off', {'broadcaster': 'low', 'b': 'low'}], 'inv': ['off', {'c': 'low'}]}
    broadcaster, signalMap, moduleType, moduleStatus = prepareSignal(file)

    while(True):
        buttonPressed += 1
        moduleStatus, lastPdPulse, lastBpPulse, lastXcPulse, lastThPulse = pressSignalButton(signalMap, moduleType, moduleStatus)
    
        if (lastPdPulse == "high" and pdCycle == 0):
            pdCycle = buttonPressed
        if (lastBpPulse == "high" and bpCycle == 0):
            bpCycle = buttonPressed
        if (lastXcPulse == "high" and xcCycle == 0):
            xcCycle = buttonPressed
        if (lastThPulse == "high" and thCycle == 0):
            thCycle = buttonPressed
        if (pdCycle > 0 and bpCycle > 0 and xcCycle > 0 and thCycle > 0):
            break
    

    print(lcm(pdCycle, bpCycle, xcCycle, thCycle))
