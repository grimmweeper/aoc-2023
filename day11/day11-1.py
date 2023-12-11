import numpy as np

file_path = 'day11.txt'

cosmic = []

def expandCosmic(cosmicArray):
    noGalaxyRow = np.where(np.all(cosmicArray == '.', axis= 1))[0]    
    expandCount = 0
    for row in noGalaxyRow:
        expandRow = cosmicArray[row + expandCount]
        cosmicArray = np.insert(cosmicArray, row + 1 + expandCount, expandRow, axis = 0)
        expandCount += 1


    noGalaxyCol = np.where(np.all(cosmicArray == '.', axis=0))[0]
    expandCount = 0
    for col in noGalaxyCol:
        expandCol = cosmicArray[:, col + expandCount]
        cosmicArray = np.insert(cosmicArray, col + expandCount + 1, expandCol, axis = 1)
        expandCount += 1
    return cosmicArray

def findAllGalaxies(cosmicArray):
    coordinates = np.column_stack(np.where(cosmicArray == '#'))
    return coordinates

def getTotalDistance(coordinatesArray):
    totalDistance = 0
    count = 0
    for i in range(len(coordinatesArray)-1):
        for j in range(i+1, len(coordinatesArray)):
            galaxyA = coordinatesArray[i]
            galaxyB = coordinatesArray[j]
            distance = abs(galaxyA[0] - galaxyB[0]) + abs(galaxyA[1] - galaxyB[1])
            totalDistance += distance
            count += 1
    return totalDistance


with open(file_path, 'r') as file:
    fileContent = file.read().strip().split("\n")
    for line in fileContent:
        cosmic.append(list(line))
    cosmicArray = np.array(cosmic)
    cosmicArray = expandCosmic(cosmicArray)
    coordinatesArray = findAllGalaxies(cosmicArray)
    totalDistance = getTotalDistance(coordinatesArray)
    print(totalDistance)

