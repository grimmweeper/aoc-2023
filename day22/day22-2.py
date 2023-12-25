from collections import deque as queue
file_path = 'day22.txt'

def prepareRawBricks(file):
    brickDict = {}
    brickId = 0
    for line in file:
        rawBrick = line.strip().split("~")
        startBrick = [int(pos) for pos in rawBrick[0].split(",")]
        endBrick = [int(pos) for pos in rawBrick[1].split(",")]
        startHeight = startBrick[2]
        if (startHeight not in brickDict):
            brickDict[startHeight] = [startBrick + endBrick + [brickId]]
        else:
            brickPair = startBrick + endBrick + [brickId]
            brickDict[startHeight].append(brickPair)
        brickId += 1
    return brickDict, brickId

def isOverlap(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

def updateBrickFinal(brick, brickFinal, start=1):
    for height in range(start, brick[5] - brick[2]+1+start):
        if (height not in brickFinal):
            brickFinal[height] = [brick]
        else:
            brickFinal[height].append(brick)
    return brickFinal

with open(file_path, 'r') as file:
    # {1: [[x1, y1, z1, x2, y2, z2, id],[...]]....}

    brickDict, totalBricks = prepareRawBricks(file)
    
    maxHeight = max(brickDict.keys())

    brickFinal = {}
    uncontactDict = {}
    singleSupportDict = {}
    supportDict = {}
    supportedDict = {}

    for brick in brickDict[min(brickDict.keys())]:
        brickFinal = updateBrickFinal(brick, brickFinal)
        uncontactDict[brick[6]] = True

    for i in range(2, maxHeight+1):
        if (i in brickDict):
            for brick in brickDict[i]:
                overlapBricks = []
                minHeightCheck = max(brickFinal.keys())
                overlap = False
                while (minHeightCheck > 0):
                    if (minHeightCheck in brickFinal):
                        for checkBrick in brickFinal[minHeightCheck]:
                            if (isOverlap(checkBrick, brick)):
                                if (checkBrick[6] in uncontactDict):
                                    del uncontactDict[checkBrick[6]]
                                overlapBricks.append(checkBrick)
                                overlap = True
                    minHeightCheck -= 1
                    if (overlap):
                        break
                    
                finalHeight = 1
                if (overlap):
                    brickSupportedBy = []
                    for overlapBrick in overlapBricks:
                        brickSupportedBy.append(overlapBrick[6])
                        if (overlapBrick[6] in supportDict):
                            supportDict[overlapBrick[6]].append(brick[6])
                        else:
                            supportDict[overlapBrick[6]] = [brick[6]]
                    supportedDict[brick[6]] = brickSupportedBy
                    if (len(overlapBricks) == 1):
                        singleSupportDict[overlapBricks[0][6]] = True
                    finalHeight = minHeightCheck + 2
                brickFinal = updateBrickFinal(brick, brickFinal, finalHeight)
                uncontactDict[brick[6]] = True

    singleSupportNumber = len(singleSupportDict.keys())
    uncontactNumber = len(uncontactDict.keys())
    disintegrateNumber = totalBricks - uncontactNumber - singleSupportNumber
    safeNumber = disintegrateNumber + uncontactNumber

    totalFallCount = 0
    for brick in list(singleSupportDict.keys()):
        fallQueue = queue()
        fallQueue.append(brick)
        brickFallDict = {}
        brickFallDict[brick] = True
        while(len(fallQueue) > 0):
            currentBrickFall = fallQueue.popleft()
            if (currentBrickFall not in supportDict):
                continue
            nextBrickFall = supportDict[currentBrickFall]
            for fallenBrick in nextBrickFall:
                supportedBrick = supportedDict[fallenBrick]
                brickStable = False
                for eachSupportedBrick in supportedBrick:
                    if (eachSupportedBrick not in brickFallDict):
                        brickStable = True
                        break
                if (not brickStable):
                    fallQueue.append(fallenBrick)
                    brickFallDict[fallenBrick] = True

        totalFallCount += len(brickFallDict.keys()) - 1
    print(totalFallCount)
            




                


