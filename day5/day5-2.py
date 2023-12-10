import sys
file_path = 'day5.txt'

sum = 0


def getMapNumber(number, mapArray):
    for map in mapArray:
        sourceRange = (map[1], map[1] + map[2] -1)
        if (number >= sourceRange[0] and number <= sourceRange[1]):
            diff = number - map[1]
            return map[0] + diff
        else:
            pass
    return number

def getMapRangeArray(start, end, mapArray):
    destArray = []
    inBetweenArray = []
    for map in mapArray:
        sourceStart = map[1]
        sourceEnd = map[1] + map[2] -1

        if start >= sourceStart and start <= sourceEnd:
            destStart = start - map[1] + map[0]
            if end >= sourceStart and end <= sourceEnd:
                destEnd = end - map[1] + map[0]
                destArray.append([destStart, destEnd])
                # print("part 1")

                return destArray
            else:
                # print("part 2")

                destEnd = map[0] + map[2] - 1
                destArray.append([destStart, destEnd])
                start = sourceEnd + 1
        
        elif end >= sourceStart and end <= sourceEnd:
            # print("part 3")

            destEnd = end - map[1] + map[0]
            destStart = map[0]
            destArray.append([destStart, destEnd])
            end = sourceStart - 1
        elif sourceStart > start and sourceEnd < end:
            # print("part 4")

            destArray.append([map[0], map[0] + map[2] - 1])
            inBetweenArray.append([map[0], map[0] + map[2] - 1])
    
    # Remaining unmapped
    # print("part 5")
    if (len(inBetweenArray) != 0):
        inBetweenArray = sorted(inBetweenArray, key=lambda x: x[0])
        for inbetween in inBetweenArray:
            if (start <= inbetween[0]):
                destArray.append([start, inbetween[0]-1])
                start = inbetween[1] + 1

    destArray.append([start, end])
    return destArray

        

def combineRange(start, end, rangeArray):
    for i in range(len(rangeArray)):
        if start >= rangeArray[i][0] and start <= rangeArray[i][1] and end > rangeArray[i][1]:
            rangeArray[i][1] = end
            return
        elif end >= rangeArray[i][0] and end <= rangeArray[i][1] and start < rangeArray[i][0]:
            rangeArray[i][0] = start
            return
    rangeArray.append([start, end])
    return

with open(file_path, 'r') as file:
    gardenDict = {}
    fileContent = file.read().strip().split("\n")
    # print(fileContent)

    # Prepare garden dictionary
    currentKey = None
    for line in fileContent:
        if line.endswith(':'):
            currentKey = line[:-1].strip()
            gardenDict[currentKey] = []
        elif "seeds:" in line:
            seedsArray = line.split(":")
            gardenDict[seedsArray[0]] = [int(value) for value in seedsArray[1].split()]
        elif line == '':
            pass
        else:
            values = [int(value) for value in line.split()]
            gardenDict[currentKey].append(values)

    rangeArray = []
    for i in range(0, len(gardenDict['seeds']), 2):
        locationArray = []
        startSeed = gardenDict['seeds'][i]
        endSeed = gardenDict['seeds'][i] + gardenDict['seeds'][i+1] -1
        combineRange(startSeed, endSeed, rangeArray)


    
    del gardenDict['seeds']
    mappingGroupArray = list(gardenDict.values())
    minNumber = sys.maxsize
    for rangePair in rangeArray:
        destArray = [[rangePair[0], rangePair[1]]]
        for i in range(len(mappingGroupArray)):
            tempDestArray = []
            for j in range(len(destArray)):
                rawDestArray = getMapRangeArray(destArray[j][0], destArray[j][1], mappingGroupArray[i])
                tempDestArray += rawDestArray
            # Add to destArray
            destArray = tempDestArray
        value = min(min(row) for row in destArray)
        if (value > 0):
            minNumber = min(minNumber, value)
        
    print(minNumber)

    
        
    

            

        