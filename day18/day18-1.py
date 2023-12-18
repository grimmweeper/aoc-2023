import numpy as np
import sys 

sys.setrecursionlimit(10**6) 
file_path = 'day18.txt'

def dig(pos, direction, number, lagoon):
    size = 1
    for _ in range(number):
        if (direction == "R"):
            pos = (pos[0], pos[1]+1)
            if (not isInBoundary(pos, lagoon)):
                lagoon = expandLagoon(lagoon, direction, size)

        elif (direction == "L"):
            pos = (pos[0], pos[1]-1)
            if (not isInBoundary(pos, lagoon)):
                lagoon = expandLagoon(lagoon, direction, size)
                pos = (pos[0], pos[1]+size)

        elif (direction == "U"):
            pos = (pos[0]-1, pos[1])
            if (not isInBoundary(pos, lagoon)):
                lagoon = expandLagoon(lagoon, direction, size)
                pos = (pos[0]+size, pos[1])
        
        elif (direction == "D"):
            pos = (pos[0]+1, pos[1])
            if (not isInBoundary(pos, lagoon)):
                lagoon = expandLagoon(lagoon, direction, size)

        lagoon[pos[0]][pos[1]] = '#'
    return lagoon, pos



def isInBoundary(pos, lagoon):
    maxRow = len(lagoon)
    maxCol = len(lagoon[0])
    
    if (pos[0] < 0 or pos[0] >= maxRow or pos[1] < 0 or pos[1] >= maxCol):
        return False
    return True

def expandLagoon(lagoon, direction, size=10):
    if (direction == "R"):
        additionalLagoon = np.full((lagoon.shape[0], size), ".", dtype=str)
        newLagoon = np.hstack((lagoon, additionalLagoon))
    elif (direction == "L"):
        additionalLagoon = np.full((lagoon.shape[0], size), ".", dtype=str)
        newLagoon = np.hstack((additionalLagoon, lagoon))
    elif (direction == "U"):
        additionalLagoon = np.full((size, lagoon.shape[1]), ".", dtype=str)
        newLagoon = np.vstack((additionalLagoon, lagoon))
    elif (direction == "D"):
        additionalLagoon = np.full((size, lagoon.shape[1]), ".", dtype=str)
        newLagoon = np.vstack((lagoon, additionalLagoon))
    return newLagoon

def checkInterior(lagoon, row, col):
    # Check right:
    isInterior = False
    for i in range(col, len(lagoon[0])):
        if (lagoon[row][i] == '#'):
            isInterior = True
            break 
    if (not isInterior):
        return False
    # Check left:
    isInterior = False
    for i in reversed(range(0, col)):
        if (lagoon[row][i] == '#'):
            isInterior = True
            break 
    if (not isInterior):
        return False
    # Check down:
    isInterior = False
    for i in range(row, len(lagoon)):
        if (lagoon[i][col] == '#'):
            isInterior = True
            break
    if (not isInterior):
        return False
    # Check up:
    isInterior = False
    for i in reversed(range(0, row)):
        if (lagoon[i][col] == '#'):
            isInterior = True
            break
    if (not isInterior):
        return False
    return True

def fillInterior(lagoon):
    for row in range(0, len(lagoon)):
        for col in range(len(lagoon[0])):
            if (lagoon[row][col] == '.'):
                hold = []
                for i in range(row, len(lagoon)):
                    for j in range(col, len(lagoon[0])):
                        if (lagoon[row][col] == '.'):
                            hold.append((row, col))
                        if (lagoon[row][col] != '.'):
                            break
                isAreaCovered = True
                for cell in hold:
                    isInterior = checkInterior(lagoon, cell[0], cell[1])
                    if (not isInterior):
                        isAreaCovered = False
                        break
                if (not isAreaCovered):
                    for cell in hold:
                        lagoon[cell[0]][cell[1]] = 'X'
                else:
                    for cell in hold:
                        lagoon[cell[0]][cell[1]] = '#'
                
    return lagoon

def getTrenchCount(lagoon):
    return (lagoon == '#').sum() + (lagoon == '.').sum()

def floodFill(row , col, old, new, lagoon):

    if row < 0 or row >= len(lagoon) or col < 0 or col >= len(lagoon[0]):
        return

    if lagoon[row][col] != old:
        return

    lagoon[row][col] = new
    
    floodFill(row+1, col, old, new, lagoon)
    floodFill(row-1, col, old, new, lagoon)
    floodFill(row, col+1, old, new, lagoon)
    floodFill(row, col-1, old, new, lagoon)

with open(file_path, 'r') as file:
    digPlan = []
    for line in file:
        digPlan.append(line.split())

    # Init lagoon
    pos = (0, 0)
    lagoon = np.array([[".", "."], [".", "."]])
    lagoon[pos[0]][pos[1]] = "#"

    for digPath in digPlan:
        lagoon, pos = dig(pos, digPath[0], int(digPath[1]), lagoon)

    for col in range(len(lagoon[0])):
        if (lagoon[0][col] == '.'):
            floodFill(0, col, '.', 'X', lagoon)
    
    for row in range(len(lagoon)):
        if (lagoon[row][0] == '.'):
            floodFill(row, 0, '.', 'X', lagoon)

    for col in range(len(lagoon[0])):
        if (lagoon[len(lagoon)-1][col] == '.'):
            floodFill(len(lagoon)-1, col, '.', 'X', lagoon)
    
    for row in range(len(lagoon)):
        if (lagoon[row][len(lagoon[0])-1] == '.'):
            floodFill(row, len(lagoon[0])-1, '.', 'X', lagoon)
    
    print(getTrenchCount(lagoon))

