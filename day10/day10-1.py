from collections import deque as queue

file_path = 'day10.txt'

def findStartPos(mapArray, element):
    for i in range(len(mapArray)):
        for j in range(len(mapArray[i])):
            if mapArray[i][j] == element:
                return (i,j)

def bfs(visitArray, mapArray, currentQueue, step):
    nextQueue = queue()

    while(len(currentQueue) > 0):
        cell = currentQueue.popleft()
        row = cell[0]
        col = cell[1]
        if (step == 0):
            visitArray[row][col] = -1
        else:
            visitArray[row][col] = step

        # Check for adjacent valid path
        adjacentPath = getAdjacentValidPipePath(row, col, mapArray)
        for path in adjacentPath:
            validPath = isPathValid(visitArray, mapArray, path[0], path[1])
            if (validPath):
                nextQueue.append(path)
    return nextQueue
    


def isPathValid(visitArray, mapArray, row, col):
    maxRow = len(mapArray)
    maxCol = len(mapArray[0])
    
    if (row < 0 or row >= maxRow or col < 0 or col >= maxCol):
        return False
    
    if (visitArray[row][col] != 0):
        return False

    return True

def getAdjacentValidPipePath(row, col, mapArray):
    adjacentPath = []
    maxRow = len(mapArray)
    maxCol = len(mapArray[0])
    currentTile = mapArray[row][col]

    isTop = False
    isBottom = False
    isRight = False
    isLeft = False

    if (currentTile == '|'):
        isTop = isTopTileValid(row, col, mapArray)
        isBottom = isBottomTileValid(row, col, mapArray, maxRow)
    
    elif (currentTile == '-'):
        isLeft = isLeftTileValid(row, col, mapArray)
        isRight = isRightTileValid(row, col, mapArray, maxCol)

    elif (currentTile == 'L'):
        isTop = isTopTileValid(row, col, mapArray)
        isRight = isRightTileValid(row, col, mapArray, maxCol)

    elif (currentTile == 'J'):
        isTop = isTopTileValid(row, col, mapArray)
        isLeft = isLeftTileValid(row, col, mapArray)

    elif (currentTile == '7'):
        isLeft = isLeftTileValid(row, col, mapArray)
        isBottom = isBottomTileValid(row, col, mapArray, maxRow)

    elif (currentTile == 'F'):
        isRight = isRightTileValid(row, col, mapArray, maxCol)
        isBottom = isBottomTileValid(row, col, mapArray, maxRow)
    
    if (isTop):
        adjacentPath.append((row-1, col))
    if (isBottom):
        adjacentPath.append((row+1, col))
    if (isLeft):
        adjacentPath.append((row, col-1))
    if (isRight):
        adjacentPath.append((row, col+1))

    return adjacentPath

    

def replaceStartPipe(row, col, mapArray):
    maxRow = len(mapArray)
    maxCol = len(mapArray[0])
    
    isTop = isTopTileValid(row, col, mapArray)
    isBottom = isBottomTileValid(row, col, mapArray, maxRow)
    isRight = isRightTileValid(row, col, mapArray, maxCol)
    isLeft = isLeftTileValid(row, col, mapArray)

    if (isTop and isBottom):
        mapArray[row][col] = '|'
    elif (isTop and isLeft):
        mapArray[row][col] = 'J'
    elif (isTop and isRight):
        mapArray[row][col] = 'L'
    elif (isLeft and isRight):
        mapArray[row][col] = '-'
    elif (isLeft and isBottom):
        mapArray[row][col] = '7'
    elif (isRight and isBottom):
        mapArray[row][col] = 'F'

def isTopTileValid(row, col, mapArray):
    r = row - 1
    c = col
    if (r >= 0):
        topTile = mapArray[r][c]
        if (topTile == '|' or topTile == '7' or topTile == 'F'):
            return True
    return False

def isBottomTileValid(row, col, mapArray, maxRow):
    r = row + 1
    c = col
    if (r < maxRow):
        bottomTile = mapArray[r][c]
        if (bottomTile == '|' or bottomTile == 'L' or bottomTile == 'J'):
            return True
    return False

def isLeftTileValid(row, col, mapArray):
    r = row
    c = col - 1
    if (c >= 0):
        leftTile = mapArray[r][c]
        if (leftTile == '-' or leftTile == 'L' or leftTile == 'F'):
            return True
    return False

def isRightTileValid(row, col, mapArray, maxCol):
    r = row
    c = col + 1
    if (c < maxCol):
        rightTile = mapArray[r][c]
        if (rightTile == '-' or rightTile == 'J' or rightTile == '7'):
            return True
    return False

with open(file_path, 'r') as file:
    mapArray = []
    step = 0
    for line in file:
        mapArray.append(list(line.strip()))
    startPos = findStartPos(mapArray, 'S')
    replaceStartPipe(startPos[0], startPos[1], mapArray)

    currentQueue = queue()
    currentQueue.append(startPos)

    # Create visitArray = zero-array
    visitArray = [[0] * len(mapArray[0]) for _ in range(len(mapArray))]

    while(True):
        currentQueue = bfs(visitArray, mapArray, currentQueue, step)
        step += 1
        if (len(currentQueue) == 0):
            break
    maxPath = max(max(row) for row in visitArray)
    print(maxPath)
