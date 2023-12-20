from shapely import Polygon
import math

file_path = 'day18.txt'

def getDigPlanFromInput(file):
    digPlan = []
    for line in file:
        hexColour = line.split()[2]
        distance = int(hexColour[2:7], 16)
        directionCode = hexColour[7:8]
        if (directionCode == '0'):
            direction = 'R'
        elif (directionCode == '1'):
            direction = 'D'
        elif (directionCode == '2'):
            direction = 'L'
        elif (directionCode == '3'):
            direction = 'U'
        digPlan.append([distance, direction])
    return digPlan

def getNewCoordinates(coords, digPath):
    if (digPath[1] == 'R'):
        return (coords[0]+digPath[0], coords[1])
    elif (digPath[1] == 'L'):
        return (coords[0]-digPath[0], coords[1])
    elif (digPath[1] == 'U'):
        return (coords[0], coords[1]+digPath[0])
    elif (digPath[1] == 'D'):
        return (coords[0], coords[1]-digPath[0])
    
def getPolygonArea(coordsArray):
    return Polygon(coordsArray).area

def getInnerPointsWithPickTheorem(area, outerPoints):
    innerPoints = area + 1 - (outerPoints / 2)
    return math.floor(innerPoints)

with open(file_path, 'r') as file:
    digPlan = getDigPlanFromInput(file)

    coords = (0,0)
    coordsArray = []
    coordsArray.append(coords)
    outerPoints = 1

    for digPath in digPlan:
        coords = getNewCoordinates(coords, digPath)
        coordsArray.append(coords)
        outerPoints += digPath[0]
    
    area = getPolygonArea(coordsArray)
    innerPoints = getInnerPointsWithPickTheorem(area, outerPoints)
    totalPoints = innerPoints + outerPoints
    print(totalPoints)