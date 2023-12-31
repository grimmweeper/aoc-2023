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

def getTrenchCount(lagoon):
    return (lagoon == '#').sum() + (lagoon == '.').sum()

def floodFillFromBorders(lagoon):
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

    floodFillFromBorders(lagoon)
    print(getTrenchCount(lagoon))

