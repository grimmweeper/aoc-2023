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

def isInBoundary(visitArray, mapArray, row, col):

    # Pairing: J <-> F = 1
    # Pairing: L <-> 7 = 1
    # Special: J -> 7 = 2
    # Special: L <-> F = 2
    # Normal: - = 1
    # Base: L, J, -
    # Check how many intersections from the top

    base = ''
    intersections = 0
    for i in reversed(range(row)):
        tile = mapArray[i][col]
        if (visitArray[i][col] != 0):
            if (base == ''):
                if (tile == '-'):
                    intersections += 1
                if (tile == 'L' or tile == 'J'):
                    base = tile
            elif (base == 'L'):
                if (tile == 'F'):
                    base = ''
                    intersections += 2
                elif (tile == '7'):
                    base = ''
                    intersections += 1
            elif (base == 'J'):
                if (tile == 'F'):
                    base = ''
                    intersections += 1
                elif (tile == '7'):
                    base = ''
                    intersections += 2

    return intersections % 2 != 0




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

    tilesBounded = 0
    for r in range(len(visitArray)):
        for c in range(len(visitArray[0])):
            if (visitArray[r][c] == 0):
                isBounded = isInBoundary(visitArray, mapArray, r, c)
                if (isBounded):
                    tilesBounded += 1
    
    print(tilesBounded)
