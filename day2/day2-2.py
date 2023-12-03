import math

file_path = 'day2.txt'

sum = 0

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open(file_path, 'r') as file:
    counter = 0
    for line in file:
        counter += 1
        gameConfig = line.split(":")[1]
        roundConfig = gameConfig.split(";")
        minBag = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for round in roundConfig:
            colourConfig = round.split(",")
            for colour in colourConfig:
                colourPair = colour.split()
                if (int(colourPair[0]) > minBag[colourPair[1]]):
                    minBag[colourPair[1]] = int(colourPair[0])

        multiplier = math.prod(minBag.values())
        sum += multiplier

        

    
    print(sum)

            

        