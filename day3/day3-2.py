import re

file_path = 'day3.txt'

sum = 0

def isAdjacentToNumber(rowStart, rowEnd, col, matrix):
    rowMin = max(rowStart - 1, 0)
    rowMax = min(rowEnd + 1, len(matrix[0])-1)
    colMin = max(col - 1, 0)
    colMax = min(col + 1, len(matrix)-1)

    for i in range(colMin, colMax+1):
        for j in range(rowMin, rowMax+1):
            if (matrix[i][j].isdigit()):
                return True
    return False


def getGearRatio(row, col, matrix):
    gearPartNumberArray = []
    for i in range(row-1, row+2):
        if (i < 0 or i >= len(matrix)):
            break
        for j in range(col-1, col+2):
            if (j < 0 or j >= len(matrix[0])):
                break
            else:
                if (matrix[i][j].isdigit()):
                    # Adj to the left
                    if (j < col):
                        # Skip if right is a number
                        if (matrix[i][j+1].isdigit()):
                            pass
                        else:
                            gearPartNumberArray.append(getPartNumber(i, j, matrix))
                    # center
                    elif (j == col):
                        # Skip if right is a number
                        if (j+1 >= len(matrix[0]) or matrix[i][j+1].isdigit()):
                            pass
                        else:
                            gearPartNumberArray.append(getPartNumber(i, j, matrix))

                    # Adj to the right
                    else:
                        gearPartNumberArray.append(getPartNumber(i, j, matrix))

    
    if (len(gearPartNumberArray) != 2):
        return 0
    else:
        return gearPartNumberArray[0] * gearPartNumberArray[1]


def getPartNumber(row, col, matrix):
    startCol = col
    partNumberArray = []
    while(True):
        if (startCol < 0):
            break
        elif(matrix[row][startCol].isdigit()):
            partNumberArray.append(matrix[row][startCol])
            startCol -= 1
        else:
            break
    partNumberArray.reverse()
    rightCol = col
    while(True):
     rightCol += 1
     if (rightCol < len(matrix[0]) and matrix[row][rightCol].isdigit()):
        partNumberArray.append(matrix[row][rightCol])
     else:
        break
    return int(''.join(partNumberArray))






with open(file_path, 'r') as file:
    fileContent = file.read().split('\n')
    cleanFile = [line for line in fileContent if line]
    engineMatrix = [list(line) for line in cleanFile]

    rowIdx = 0
    while (rowIdx < len(engineMatrix)):
        colIdx = 0
        while (colIdx < len(engineMatrix[0])):
            if(engineMatrix[rowIdx][colIdx] == '*'):
                gearRatio = getGearRatio(rowIdx, colIdx, engineMatrix)
                sum += gearRatio
            colIdx += 1
        rowIdx += 1
        
    
print(sum)
            

    