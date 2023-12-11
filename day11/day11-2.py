import numpy as np

file_path = 'day11.txt'

cosmic = []

def getEmptyRows(cosmicArray):
    return np.where(np.all(cosmicArray == '.', axis= 1))[0]

def getEmptyCols(cosmicArray):
    return np.where(np.all(cosmicArray == '.', axis=0))[0]

def findAllGalaxies(cosmicArray):
    coordinates = np.column_stack(np.where(cosmicArray == '#'))
    return coordinates

def getTotalDistance(coordinatesArray, emptyRows, emptyCols, expandFactor):
    totalDistance = 0
    count = 0
    for i in range(len(coordinatesArray)-1):
        for j in range(i+1, len(coordinatesArray)):
            galaxyA = coordinatesArray[i]
            galaxyB = coordinatesArray[j]
            
            rowExpandCount = 0
            for row in emptyRows:
                if (row > galaxyA[0] and row < galaxyB[0]):
                    rowExpandCount += 1
            
            colExpandCount = 0
            for col in emptyCols:
                if (galaxyA[1] > galaxyB[1]):
                    if (galaxyA[1] > col and col > galaxyB[1]):
                        colExpandCount += 1
                elif (galaxyB[1] > galaxyA[1]):
                    if (galaxyB[1] > col and col > galaxyA[1]):
                        colExpandCount += 1

            distance = abs(galaxyA[0] - galaxyB[0]) + (expandFactor - 1)*rowExpandCount + abs(galaxyA[1] - galaxyB[1]) + (expandFactor - 1)*colExpandCount
            totalDistance += distance
            count += 1
    return totalDistance


with open(file_path, 'r') as file:
    fileContent = file.read().strip().split("\n")
    for line in fileContent:
        cosmic.append(list(line))
    cosmicArray = np.array(cosmic)
    coordinatesArray = findAllGalaxies(cosmicArray)
    emptyRows = getEmptyRows(cosmicArray)
    emptyCols = getEmptyCols(cosmicArray)
    totalDistance = getTotalDistance(coordinatesArray, emptyRows, emptyCols, 1000000)
    print(totalDistance)

