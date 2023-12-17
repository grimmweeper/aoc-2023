import numpy as np

file_path = 'day14.txt'

def shiftRockToEmptySpace(tempRockPosArray, fixedRockPos, row, col):
    flexiRockNumber = len(tempRockPosArray)
    for i in range(fixedRockPos[0] + 1, row):
        if (flexiRockNumber > 0):
            dishArray[i][col] = 'O'
            flexiRockNumber -= 1
        else:
            dishArray[i][col] = '.'

def tiltNorth(dishArray):
    for col in range(len(dishArray[0])):
        tempRockPosArray = []
        fixedRockPos = (-1, col)
        for row in range(len(dishArray)):
            if (dishArray[row][col] == 'O'):
                tempRockPosArray.append((row, col))
            elif (dishArray[row][col] == '#'):
                shiftRockToEmptySpace(tempRockPosArray, fixedRockPos, row, col)
                tempRockPosArray = []
                fixedRockPos = (row, col)
        shiftRockToEmptySpace(tempRockPosArray, fixedRockPos, row+1, col)
        

def calculateLoad(dishArray):
    totalLoad = 0
    loadMultiplier = len(dishArray)
    for row in range(len(dishArray)):
        rockCount = np.count_nonzero(dishArray[row] == 'O')
        rockWeight = rockCount * loadMultiplier
        totalLoad += rockWeight
        loadMultiplier -= 1
    return totalLoad



with open(file_path, 'r') as file:
    dish = []
    fileContent = file.read().strip().split("\n")
    for line in fileContent:
        dish.append(list(line))
    dishArray = np.array(dish)
    # print(dishArray)
    tiltNorth(dishArray)
    totalLoad = calculateLoad(dishArray)
    print(totalLoad)
