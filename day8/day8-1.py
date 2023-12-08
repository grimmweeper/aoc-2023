file_path = 'day8.txt'

def traverseNetwork(instructions, networkDict, current, step):
    for direction in instructions:
        if current == 'ZZZ':
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

    fileContent = file.read().strip().split("\n")
    instructions = fileContent[0]

    # Prepare network dictionary
    for i in range(2, len(fileContent)):
        network = fileContent[i].split('=')
        nextNodeArray = network[1].strip().split(',')
        nextNodeLeft = nextNodeArray[0].strip().replace("(", "")
        nextNodeRight = nextNodeArray[1].strip().replace(")", "")
        networkDict[network[0].strip()] = (nextNodeLeft, nextNodeRight)
    
    current = 'AAA'
    step = traverseNetwork(instructions, networkDict, current, step)
    print(step)
