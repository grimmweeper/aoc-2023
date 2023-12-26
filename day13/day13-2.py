import numpy as np
import math
from copy import deepcopy

file_path = 'day13.txt'

def getVerticalReflectionLine(lava, oldColNum = -1):
    maxCol = len(lava[0])
    for i in range(math.floor(maxCol/2)):
        # Check from left
        colLeft = lava[:, :i+1]
        colRight = lava[:, i+1:2*(i+1)]
        colRightFlip = np.fliplr(colRight)
        if (checkArrayIdentical(colLeft, colRightFlip)):
            colNum = i + 1
            if (colNum != oldColNum):
                return colNum

        # Check from right
        colLeft = lava[:, maxCol-2*(i+1):maxCol-i-1]
        colRight = lava[:, maxCol-i-1:]
        colRightFlip = np.fliplr(colRight)
        if (checkArrayIdentical(colLeft, colRightFlip)):
            colNum = maxCol - 1 - i
            if (colNum != oldColNum):
                return colNum
    return 0

def getHorizontalReflectionLine(lava, oldRowNum = -1):
    maxRow = len(lava)
    for i in range(math.floor(maxRow/2)):
        # Check from top
        rowTop = lava[:i+1, :]
        rowBottom = lava[i+1:2*(i+1), :]
        rowBottomFlip = np.flipud(rowBottom)
        if (checkArrayIdentical(rowTop, rowBottomFlip)):
            rowNum = i + 1
            if (rowNum != oldRowNum):
                return rowNum

        # Check from bottom
        rowTop = lava[maxRow-2*(i+1):maxRow-i-1, :]
        rowBottom = lava[maxRow-i-1:, :]
        rowBottomFlip = np.flipud(rowBottom)
        if (checkArrayIdentical(rowTop, rowBottomFlip)):
            rowNum = maxRow - 1 - i
            if (rowNum != oldRowNum):
                return rowNum
    return 0   

def checkArrayIdentical(subArray1, subArray2):
    return np.array_equal(subArray1, subArray2)


with open(file_path, 'r') as file:
    lavaArray = []
    lava = []
    summary = 0
    for line in file:
        if (len(line.strip()) == 0):
            lavaArray.append(lava)
            lava = []
        else:
            lava.append(list(line.strip()))
    lavaArray.append(lava)

    for lava in lavaArray:
        lava = np.array(lava)
        foundSmudge = False
        numCol = getVerticalReflectionLine(lava)
        numRow = getHorizontalReflectionLine(lava)
        for row in range(len(lava)):
            for col in range(len(lava[0])):
                newLava = deepcopy(lava)
                if (newLava[row][col] == "#"):
                    newLava[row][col] = "."
                else:
                    newLava[row][col] = "#"
                numColNew = getVerticalReflectionLine(newLava, numCol)
                numRowNew = getHorizontalReflectionLine(newLava, numRow)

                if (numColNew > 0):
                    summary += numColNew
                    foundSmudge = True
                    break
                
                if (numRowNew > 0):
                    summary += numRowNew*100
                    foundSmudge = True
                    break

            if (foundSmudge):
                break
    print(summary)