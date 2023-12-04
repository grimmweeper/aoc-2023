file_path = 'day4.txt'

sum = 0

copiesDict = {}

with open(file_path, 'r') as file:
    counter = 1
    for line in file:
        if (counter not in copiesDict):
            copiesDict[counter] = 1
        else:
            copiesDict[counter] += 1
        
        matchingNumber = 0
        points = 0
        cardRow = line.split(":")[1].split("|")
        winningNumber = cardRow[0].split()
        scratchCard = cardRow[1].split()
        

        for number in scratchCard:
            if (number in winningNumber):
                matchingNumber += 1
        
        for i in range(1, matchingNumber+1):
            if (i+counter not in copiesDict):
                copiesDict[i+counter] = copiesDict[counter]
            else:
                copiesDict[i+counter] += copiesDict[counter]

        sum += copiesDict[counter]
        counter += 1
    print(copiesDict)
    print(sum)

            

        