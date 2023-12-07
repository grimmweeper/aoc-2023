import functools

file_path = 'day7.txt'

cardStrength = {
    'A': 1,
    'K': 2,
    'Q': 3,
    'T': 5,
    '9': 6,
    '8': 7,
    '7': 8,
    '6': 9,
    '5': 10,
    '4': 11,
    '3': 12,
    '2': 13,
    'J': 14,
}

# hand = 'AAAAA'
def getCardFrequency(hand):
    cardFrequency = {}
    for card in hand:
        if card in cardFrequency:
            cardFrequency[card] += 1
        else:
            cardFrequency[card] = 1
    return cardFrequency

def accountForJoker(cardFrequency):
    frequencyArray = list(cardFrequency.values())
    maxFrequency = max(frequencyArray)
    
    if 'J' in cardFrequency:
        
        
        # {'J': 1, 'Q': 2, 'A': 2} => {'Q': 3, 'A': 2}
        # Joker is not the max: Add to max frequency letter
        if maxFrequency != cardFrequency['J']:
            card = [k for k, v in cardFrequency.items() if v == maxFrequency]
            cardFrequency[card[0]] += cardFrequency['J']
            del cardFrequency['J']
    
        # {'J': 3, 'Q': 1, 'A': 1} => {'Q': 4, 'A': 1}
        # Joker is the max: Add to the next highest max frequency letter
        elif cardFrequency['J'] < 5:
            frequencyArray.remove(maxFrequency)
            newMaxFrequency = max(frequencyArray)
            card = [k for k, v in cardFrequency.items() if v == newMaxFrequency]
            if 'J' in card:
                card.remove('J')
            cardFrequency[card[0]] += cardFrequency['J']
            del cardFrequency['J']

    return cardFrequency


def getHandTypeStrength(hand):
    cardFrequency = getCardFrequency(hand)
    newCardFrequency = accountForJoker(cardFrequency)
    frequencyArray = list(newCardFrequency.values())
    maxFrequency = max(frequencyArray)
    if maxFrequency == 5:
        # 5-of-a-kind
        return 1
    elif maxFrequency == 4:
        # 4-of-a-kind
        return 2
    elif maxFrequency == 3:
        if 2 in frequencyArray:
            # full-house
            return 3
        else:
            # 3-of-a-kind
            return 4
    elif maxFrequency == 2:
        if frequencyArray.count(2) == 2:
            # two-pair
            return 5
        else:
            # one-pair
            return 6
    else:
        # high-card
        return 7

def compareHand(hand1, hand2):
    handStrength1 = getHandTypeStrength(hand1)
    handStrength2 = getHandTypeStrength(hand2)

    if (handStrength1 == handStrength2):
        # Compare individual card
        for card1, card2 in zip(hand1, hand2):
            if card1 == card2:
                continue
            else:
                return cardStrength[card2] - cardStrength[card1]

    else:
        return handStrength2 - handStrength1


with open(file_path, 'r') as file:
    totalWinnings = 0
    handArray = []
    handBidDict = {}
    for line in file:
        lineArray = line.split()
        handArray.append(lineArray[0])
        handBidDict[lineArray[0]] = int(lineArray[1])

    # print(handArray)
    # print(handBidDict)

    # Sort hand size from weakest to strongest
    cmp = functools.cmp_to_key(compareHand)
    weakToStrongHandSize = sorted(handArray, key=cmp)
    # print(weakToStrongHandSize)

    for i in range(len(weakToStrongHandSize)):
        winnings = handBidDict[weakToStrongHandSize[i]] * (i+1)
        totalWinnings += winnings
    print(totalWinnings)

