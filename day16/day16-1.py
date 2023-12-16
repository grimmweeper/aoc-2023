from collections import deque as queue

file_path = 'day16.txt'

class Beam:
    def __init__(self, _row, _col, _direction) -> None:
        self.row = _row
        self.col = _col
        self.direction = _direction

    def __eq__(self, other): 
        if not isinstance(other, Beam):
            return False

        return self.row == other.row and self.col == other.col and self.direction == other.direction

    def output(self):
        print(self.row, self.col, self.direction)

def inBoundary(row, col, maxRow, maxCol):
    if (row < 0 or row >= maxRow or col < 0 or col >= maxCol):
        return False
    return True

def moveRightBeam(beam: Beam):
    newRow = beam.row
    newCol = beam.col + 1
    newDirection = "right"
    newBeam = Beam(newRow, newCol, newDirection)
    return newBeam

def moveLeftBeam(beam: Beam):
    newRow = beam.row
    newCol = beam.col - 1
    newDirection = "left"
    newBeam = Beam(newRow, newCol, newDirection)
    return newBeam

def moveUpBeam(beam: Beam):
    newRow = beam.row - 1
    newCol = beam.col
    newDirection = "up"
    newBeam = Beam(newRow, newCol, newDirection)
    return newBeam

def moveDownBeam(beam: Beam):
    newRow = beam.row + 1
    newCol = beam.col
    newDirection = "down"
    newBeam = Beam(newRow, newCol, newDirection)
    return newBeam

def updateBeamQueue(beam: Beam, beamQueue, mapArray):
    maxRow = len(mapArray)
    maxCol = len(mapArray[0])

    beamObject = mapArray[beam.row][beam.col]

    if (beam.direction == "right"):
        if (beamObject == "/"):
            newBeamArray = [moveUpBeam(beam)]
        elif (beamObject == "\\"):
            newBeamArray = [moveDownBeam(beam)]
        elif (beamObject == "|"):
            newBeamArray = [moveUpBeam(beam), moveDownBeam(beam)]
        else:
            newBeamArray = [moveRightBeam(beam)]
    
    elif (beam.direction == "left"):
        if (beamObject == "/"):
            newBeamArray = [moveDownBeam(beam)]
        elif (beamObject == "\\"):
            newBeamArray = [moveUpBeam(beam)]
        elif (beamObject == "|"):
            newBeamArray = [moveUpBeam(beam), moveDownBeam(beam)]
        else:
            newBeamArray = [moveLeftBeam(beam)]

    elif (beam.direction == "up"):
        if (beamObject == "/"):
            newBeamArray = [moveRightBeam(beam)]
        elif (beamObject == "\\"):
            newBeamArray = [moveLeftBeam(beam)]
        elif (beamObject == "-"):
            newBeamArray = [moveLeftBeam(beam), moveRightBeam(beam)]
        else:
            newBeamArray = [moveUpBeam(beam)]

    elif (beam.direction == "down"):
        if (beamObject == "/"):
            newBeamArray = [moveLeftBeam(beam)]
        elif (beamObject == "\\"):
            newBeamArray = [moveRightBeam(beam)]
        elif (beamObject == "-"):
            newBeamArray = [moveLeftBeam(beam), moveRightBeam(beam)]
        else:
            newBeamArray = [moveDownBeam(beam)]
    
    for newBeam in newBeamArray:
        if (inBoundary(newBeam.row, newBeam.col, maxRow, maxCol)):
            beamQueue.append(newBeam)
    return beamQueue


def updateBeamArrayWithloopDetection(beamArray, currentBeam):
    isBeamExist = False
    beamPathTracker = beamArray[currentBeam.row][currentBeam.col]
    
    if (beamPathTracker == 0):
        beamArray[currentBeam.row][currentBeam.col] = [currentBeam]
    else:
        for beamTrackerElement in beamPathTracker:
            if (beamTrackerElement == currentBeam):
                isBeamExist = True
                break
        beamArray[currentBeam.row][currentBeam.col].append(currentBeam)
    return isBeamExist

def getEnergisedCount(beamArray):
    energisedCount = 0
    for beamArrayRow in beamArray:
        for beamElement in beamArrayRow:
            if (beamElement != 0):
                energisedCount += 1
    return energisedCount

with open(file_path, 'r') as file:
    mapArray = []
    for line in file:
        mapArray.append(list(line.strip()))

    beamQueue = queue()
    # Create beamArray = zero-array
    beamArray = [[0] * len(mapArray[0]) for _ in range(len(mapArray))]

    initialBeam = Beam(0, 0, "right")
    beamQueue.append(initialBeam)
    while (len(beamQueue) > 0):
        currentBeam = beamQueue.popleft()
        loopDetected = updateBeamArrayWithloopDetection(beamArray, currentBeam)
        if (not loopDetected):
            beamQueue = updateBeamQueue(currentBeam, beamQueue, mapArray)

    energisedCount = getEnergisedCount(beamArray)
    print(energisedCount)



