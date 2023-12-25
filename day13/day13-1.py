import numpy as np
import math

file_path = 'day13.txt'

def getVerticalReflectionLine(lava):
    maxCol = len(lava[0])
    for i in range(math.floor(maxCol/2)):
        # Check from left
        colLeft = lava[:, :i+1]
        colRight = lava[:, i+1:2*(i+1)]
        colRightFlip = np.fliplr(colRight)
        if (checkArrayIdentical(colLeft, colRightFlip)):
            return i + 1

        # Check from right
        colLeft = lava[:, maxCol-2*(i+1):maxCol-i-1]
        colRight = lava[:, maxCol-i-1:]
        colRightFlip = np.fliplr(colRight)
        if (checkArrayIdentical(colLeft, colRightFlip)):
            return maxCol - 1 - i
    return 0

def getHorizontalReflectionLine(lava):
    maxRow = len(lava)
    for i in range(math.floor(maxRow/2)):
        # Check from top
        rowTop = lava[:i+1, :]
        rowBottom = lava[i+1:2*(i+1), :]
        rowBottomFlip = np.flipud(rowBottom)
        if (checkArrayIdentical(rowTop, rowBottomFlip)):
            return i + 1

        # Check from bottom
        rowTop = lava[maxRow-2*(i+1):maxRow-i-1, :]
        rowBottom = lava[maxRow-i-1:, :]
        rowBottomFlip = np.flipud(rowBottom)
        if (checkArrayIdentical(rowTop, rowBottomFlip)):
            return maxRow - 1 - i
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
        numCol = getVerticalReflectionLine(lava)
        numRow = getHorizontalReflectionLine(lava)
        summary += (numCol + numRow*100)
    print(summary)