from collections import deque as queue

file_path = 'day17.txt'

class Heat:
    def __init__(self, _row, _col, _value, _direction) -> None:
        self.row = _row
        self.col = _col
        self.value = _value
        self.direction = _direction

def moveRight(heat: Heat, directionChange: bool):
    newRow = heat.row
    newCol = heat.col + 1
    if (directionChange):
        newDirection = ("right", 1)
    else:
        newDirection = ("right", heat.direction[1] + 1)
    newHeat = Heat(newRow, newCol, heat.value, newDirection)
    return newHeat

def moveLeft(heat: Heat, directionChange: bool):
    newRow = heat.row
    newCol = heat.col - 1
    if (directionChange):
        newDirection = ("left", 1)
    else:
        newDirection = ("left", heat.direction[1] + 1)
    newHeat = Heat(newRow, newCol, heat.value, newDirection)
    return newHeat

def moveUp(heat: Heat, directionChange: bool):
    newRow = heat.row - 1
    newCol = heat.col
    if (directionChange):
        newDirection = ("up", 1)
    else:
        newDirection = ("up", heat.direction[1] + 1)
    newHeat = Heat(newRow, newCol, heat.value, newDirection)
    return newHeat

def moveDown(heat: Heat, directionChange: bool):
    newRow = heat.row + 1
    newCol = heat.col
    if (directionChange):
        newDirection = ("down", 1)
    else:
        newDirection = ("down", heat.direction[1] + 1)
    newHeat = Heat(newRow, newCol, heat.value, newDirection)
    return newHeat

def isValidMove(heat: Heat, maxRow, maxCol):
    if (heat.row < 0 or heat.row >= maxRow or heat.col < 0 or heat.col >= maxCol):
        return False
    if (heat.direction[1] > 10):
        return False
    return True

def updateHeatQueue(heat: Heat, heatQueue, mapArray):
    maxRow = len(mapArray)
    maxCol = len(mapArray[0])

    if (heat.direction[0] == "right"):
        if (heat.direction[1] < 4):
            newHeatArray = [moveRight(heat, False)]
        else:
            newHeatArray = [moveDown(heat, True), moveUp(heat, True), moveRight(heat, False)]
    elif (heat.direction[0] == "left"):
        if (heat.direction[1] < 4):
            newHeatArray = [moveLeft(heat, False)]
        else:
            newHeatArray = [moveDown(heat, True), moveUp(heat, True), moveLeft(heat, False)]
    elif (heat.direction[0] == "up"):
        if (heat.direction[1] < 4):
            newHeatArray = [moveUp(heat, False)]
        else:
            newHeatArray = [moveRight(heat, True), moveLeft(heat, True), moveUp(heat, False)]
    elif (heat.direction[0] == "down"):
        if (heat.direction[1] < 4):
            newHeatArray = [moveDown(heat, False)]
        else:
            newHeatArray = [moveRight(heat, True), moveLeft(heat, True), moveDown(heat, False)]

    for newHeat in newHeatArray:
        if (isValidMove(newHeat, maxRow, maxCol)):
            newHeat.value += mapArray[newHeat.row][newHeat.col]
            heatQueue.append(newHeat)
    return heatQueue




with open(file_path, 'r') as file:
    mapArray = []
    for line in file:
        mapArray.append(list(int(line) for line in line.strip()))

    heatQueue = queue()
    # Create heatArray = zero-array
    heatArray = [[0] * len(mapArray[0]) for _ in range(len(mapArray))]

    initialHeatRight = Heat(0, 0, 0, ("right", 0))
    initialHeatDown = Heat(0, 0, 0, ("down", 0))
    heatQueue.append(initialHeatRight)
    heatQueue.append(initialHeatDown)

    while(len(heatQueue) > 0):
        currentHeat: Heat = heatQueue.popleft()

        isLessHeat = True
        heatTracker = heatArray[currentHeat.row][currentHeat.col]
        
        if (heatTracker == 0):
            heatArray[currentHeat.row][currentHeat.col] = [[currentHeat.value], [currentHeat.direction]]
        else:
            heatValueUpdated = False
            for i in range(len(heatTracker[1])):
                if (currentHeat.direction == heatTracker[1][i]):
                    if (currentHeat.value < heatTracker[0][i]):
                        heatArray[currentHeat.row][currentHeat.col][0][i] = currentHeat.value
                        heatValueUpdated = True
                    else:
                        isLessHeat = False
                    break

            if (isLessHeat and not heatValueUpdated):
                heatArray[currentHeat.row][currentHeat.col][0].append(currentHeat.value)
                heatArray[currentHeat.row][currentHeat.col][1].append(currentHeat.direction)
            
        if (isLessHeat):
            heatQueue = updateHeatQueue(currentHeat, heatQueue, mapArray)
    
    endHeatPath = heatArray[-1][-1]

    minHeatValue = 1000000
    for i in range(len(endHeatPath[0])):
        if (endHeatPath[1][i][1] < 4):
            pass
        else:
            minHeatValue = min(minHeatValue, endHeatPath[0][i])
    print(minHeatValue)
