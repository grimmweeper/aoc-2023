file_path = 'day15.txt'

def getHashValue(word):
    hashValue = 0
    for char in word:
        hashValue += ord(char)
        hashValue *= 17
        hashValue %= 256
    return hashValue

def addLensToBox(boxDict, labelHash, label):
    if labelHash in boxDict:
        isBoxUpdated = False
        box = boxDict[labelHash]
        for i in range(len(box)):
            if (label[0] == box[i][0]):
                boxDict[labelHash][i] = (label[0], int(label[1]))
                isBoxUpdated = True
                break
        if (not isBoxUpdated):
            boxDict[labelHash].append((label[0], int(label[1])))
    else:
        boxDict[labelHash] = [(label[0], int(label[1]))]

def removeLensFromBox(boxDict, labelHash, label):
    if labelHash in boxDict:
        for i in range(len(boxDict[labelHash])):
            if label == boxDict[labelHash][i][0]:
                boxDict[labelHash].pop(i)
                break

def getFocusPower(boxDict):
    totalFocusPower = 0
    for i in range(256):
        if (i in boxDict):
            boxArray = boxDict[i]
            for j in range(len(boxArray)):
                focusPower = (i+1) * (j+1) * boxArray[j][1]
                totalFocusPower += focusPower
    return totalFocusPower

with open(file_path, 'r') as file:
    wordArray = list(file.read().strip().split(","))
    # print(wordArray)
    # Data structure for box: { 0: [("rn", 1), ("cm", 2)], 1: [("qp": 3)] ...}
    boxDict = {}
    for word in wordArray:
        if "=" in word:  
            label = word.split("=")
            labelHash = getHashValue(label[0])
            addLensToBox(boxDict, labelHash, label)

        elif "-" in word:
            label = word.split("-")
            labelHash = getHashValue(label[0])
            removeLensFromBox(boxDict, labelHash, label[0])

    totalFocusPower = getFocusPower(boxDict)
    print(totalFocusPower)


    