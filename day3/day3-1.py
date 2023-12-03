import re

file_path = 'day3.txt'

sum = 0

def isAdjacentToSymbol(rowStart, rowEnd, col, matrix):
    rowMin = max(rowStart - 1, 0)
    rowMax = min(rowEnd + 1, len(matrix[0])-1)
    colMin = max(col - 1, 0)
    colMax = min(col + 1, len(matrix)-1)

    for i in range(colMin, colMax+1):
        for j in range(rowMin, rowMax+1):
            if (isSymbol(matrix[i][j])):
                return True
    return False

def isSymbol(element):
    pattern = re.compile(r'[^A-Za-z0-9.]')
    return bool(pattern.match(element))

def getPartNumber(rowStart, col, matrix, partNumberArray=[]):
    if (matrix[col][rowStart].isdigit()):
        partNumberArray.append(matrix[col][rowStart])
        rowStart += 1
        if (rowStart >= len(matrix[0])):
            return (int(''.join(partNumberArray)), rowStart - 1)
        return getPartNumber(rowStart, col, matrix, partNumberArray)
    else:
        return (int(''.join(partNumberArray)), rowStart - 1)



with open(file_path, 'r') as file:
    fileContent = file.read().split('\n')
    cleanFile = [line for line in fileContent if line]
    engineMatrix = [list(line) for line in cleanFile]

    colIdx = 0
    while (colIdx < len(engineMatrix)):
        rowIdx = 0
        while (rowIdx < len(engineMatrix[0])):
            if(engineMatrix[colIdx][rowIdx].isdigit()):
                rowStart = rowIdx
                partNumber, rowIdx = getPartNumber(rowIdx, colIdx, engineMatrix, [])
                rowEnd = rowIdx
                if (isAdjacentToSymbol(rowStart, rowEnd, colIdx, engineMatrix)):
                    sum += partNumber

            rowIdx += 1


        colIdx += 1
        
    
print(sum)
            

    