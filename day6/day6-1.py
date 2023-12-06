import cmath
import math

def solveQuadratic(a, b, c):
    # Calculate the discriminant
    delta = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the two solutions using the quadratic formula
    root1 = (-b + delta.real) / (2 * a)
    root2 = (-b - delta.real) / (2 * a)

    return root1, root2

def getNumberOfWaysToMatchRecord(duration, distance):
    holdMin, holdMax = solveQuadratic(-1, duration, distance * -1)
    holdRange = range(math.ceil(min(holdMin, holdMax)), math.floor(max(holdMin, holdMax)) + 1)
    return len(holdRange)

file_path = 'day6.txt'
raceDict = {}
product = 1

with open(file_path, 'r') as file:
    fileContent = file.read().strip().split("\n")
    for content in fileContent:
        contentArray = content.split(":")
        raceDict[contentArray[0]] = [int(value) for value in contentArray[1].split()]

    for i in range(len(raceDict['Time'])):
        ways = getNumberOfWaysToMatchRecord(raceDict['Time'][i], raceDict['Distance'][i]+1)
        product *= ways
    
    print(product)


    

    
        
    

            

        