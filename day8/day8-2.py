import sys
import math
sys.setrecursionlimit(100000)

file_path = 'day8.txt'


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcmArray(numberArray):
    result = 1
    for number in numberArray:
        result = lcm(result, number)
    return result

def traverseNetwork(instructions, networkDict, current, step):
    for direction in instructions:
        if current.endswith('Z'):
            return step
        if direction == 'L':
            current = networkDict[current][0]
        elif direction == 'R':
            current = networkDict[current][1]
        step += 1
    return traverseNetwork(instructions, networkDict, current, step)

with open(file_path, 'r') as file:
    networkDict = {}
    step = 0
    startArray = []
    stepArray = []

    fileContent = file.read().strip().split("\n")
    instructions = fileContent[0]

    # Prepare network dictionary
    for i in range(2, len(fileContent)):
        network = fileContent[i].split('=')
        nextNodeArray = network[1].strip().split(',')
        nextNodeLeft = nextNodeArray[0].strip().replace("(", "")
        nextNodeRight = nextNodeArray[1].strip().replace(")", "")
        networkDict[network[0].strip()] = (nextNodeLeft, nextNodeRight)

        if network[0].strip().endswith('A'):
            startArray.append(network[0].strip())
    

    for start in startArray:
        step = traverseNetwork(instructions, networkDict, start, step)
        stepArray.append(step)
        step = 0
    
    minStep = lcmArray(stepArray)
    print(minStep)

