import numpy as np

file_path = 'day14.txt'

def shiftVerticalRock(tempRockPosArray, fixedRockPos, row, col, direction):
    flexiRockNumber = len(tempRockPosArray)
    rockRange = range(fixedRockPos[0] + 1, row)
    if (direction == "south"):
        rockRange = reversed(rockRange)
    for i in rockRange:
        if (flexiRockNumber > 0):
            dishArray[i][col] = 'O'
            flexiRockNumber -= 1
        else:
            dishArray[i][col] = '.'

def shiftHorizontalRock(tempRockPosArray, fixedRockPos, row, col, direction="west"):
    flexiRockNumber = len(tempRockPosArray)
    rockRange = range(fixedRockPos[1] + 1, col)
    if (direction == "east"):
        rockRange = reversed(rockRange)
    for i in rockRange:
        if (flexiRockNumber > 0):
            dishArray[row][i] = 'O'
            flexiRockNumber -= 1
        else:
            dishArray[row][i] = '.'

def tiltVertical(dishArray, direction):
    for col in range(len(dishArray[0])):
        tempRockPosArray = []
        fixedRockPos = (-1, col)
        for row in range(len(dishArray)):
            if (dishArray[row][col] == 'O'):
                tempRockPosArray.append((row, col))
            elif (dishArray[row][col] == '#'):
                shiftVerticalRock(tempRockPosArray, fixedRockPos, row, col, direction)
                tempRockPosArray = []
                fixedRockPos = (row, col)
        shiftVerticalRock(tempRockPosArray, fixedRockPos, row+1, col, direction)
        

def tiltHorizontal(dishArray, direction):
    for row in range(len(dishArray)):
        tempRockPosArray = []
        fixedRockPos = (row, -1)
        for col in range(len(dishArray[row])):
            if (dishArray[row][col] == 'O'):
                tempRockPosArray.append((row, col))
            elif (dishArray[row][col] == '#'):
                shiftHorizontalRock(tempRockPosArray, fixedRockPos, row, col, direction)
                tempRockPosArray = []
                fixedRockPos = (row, col)
        shiftHorizontalRock(tempRockPosArray, fixedRockPos, row, col+1, direction)

def getLoadWithSpinCycle(dishArray, cycles):
    loadArray = []
    for i in range(500):
        tiltVertical(dishArray, "north")
        tiltHorizontal(dishArray, "west")
        tiltVertical(dishArray, "south")
        tiltHorizontal(dishArray, "east")
        # Wait for it to stabilise
        if (i >= 249):
            loadArray.append(calculateLoad(dishArray))
    return getLoadFromCycleDetection(loadArray, cycles)



def calculateLoad(dishArray):
    totalLoad = 0
    loadMultiplier = len(dishArray)
    for row in range(len(dishArray)):
        rockCount = np.count_nonzero(dishArray[row] == 'O')
        rockWeight = rockCount * loadMultiplier
        totalLoad += rockWeight
        loadMultiplier -= 1
    return totalLoad

def getLoadFromCycleDetection(loadArray, cycles):
    loadArray = np.array(loadArray)
    loadDict = {}
    for i in range(len(loadArray)):
        if loadArray[i] in loadDict:
            loadDict[loadArray[i]].append(i)
        else:
            loadDict[loadArray[i]] = [i]

    minArrayKey = min(loadDict, key=lambda k: len(loadDict[k]))
    cycleLoop = loadDict[minArrayKey][1] - loadDict[minArrayKey][0]
    cycleArray = []
    for i in range(cycleLoop):
        cycleArray.append(loadArray[i+cycleLoop])

    iteration = (cycles - 250) % cycleLoop
    return cycleArray[iteration]

with open(file_path, 'r') as file:
    dish = []
    fileContent = file.read().strip().split("\n")
    for line in fileContent:
        dish.append(list(line))
    dishArray = np.array(dish)

    totalLoad = getLoadWithSpinCycle(dishArray, 1000000000)
    print(totalLoad)

