file_path = 'day4.txt'

sum = 0

with open(file_path, 'r') as file:
    for line in file:
        points = 0
        cardRow = line.split(":")[1].split("|")
        winningNumber = cardRow[0].split()
        scratchCard = cardRow[1].split()
        for number in scratchCard:
            if (number in winningNumber):
                if (points == 0):
                    points += 1
                else:
                    points *= 2
        sum += points
    print(sum)

            

        