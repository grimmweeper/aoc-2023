file_path = 'day9.txt'

def allZeros(arr):
    return all(element == 0 for element in arr)

def getNextDiffArray(currentDiffArray):
    nextDiffArray = []
    for i in range(len(currentDiffArray) - 1):
        diff = currentDiffArray[i+1] - currentDiffArray[i]
        nextDiffArray.append(diff)
    return nextDiffArray

def predictHistoryValue(historyArray):
    diffArrayCollector = []
    currentDiffArray = historyArray
    while (True):
        nextDiffArray = getNextDiffArray(currentDiffArray)
        diffArrayCollector.append(nextDiffArray)
        if (allZeros(nextDiffArray)):
            break
        currentDiffArray = nextDiffArray
    lastValue = 0
    for diffArray in reversed(diffArrayCollector):
        lastValue = diffArray[0] - lastValue
    return historyArray[0] - lastValue



with open(file_path, 'r') as file:

    sumValue = 0 
    
    for line in file:
        historyArray = [int(value) for value in line.split()]
        historyValue = predictHistoryValue(historyArray)
        sumValue += historyValue
    
    print(sumValue)
