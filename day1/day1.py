file_path = 'day1.txt'

sum = 0

def getDigitFromLetterDigits(numDict, word):
    numArray = list(numDict.keys())
    for num in numArray:
        if num in word:
            return numDict[num]
    


with open(file_path, 'r') as file:
    for word in file:

        # Assign flags for forward and reverse iterations
        forwardStop = False
        reverseStop = False

        firstDigit = ''
        secondDigit = ''

        wordLength = len(word)

        numDict = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }


        for i in range(wordLength):
            reverseIdx = wordLength - 1 - i

            forwardString = word[:i+1]
            if (not forwardStop):
                if (word[i].isdigit()):
                    firstDigit = word[i]
                    forwardStop = True
                else:
                    potentialFirstDigit = getDigitFromLetterDigits(numDict, forwardString)
                    if (potentialFirstDigit is not None):
                        firstDigit = potentialFirstDigit
                        forwardStop = True


            reverseString = word[(i+1)*-1:]
            if (not reverseStop):
                if (word[reverseIdx].isdigit()):
                    secondDigit = word[reverseIdx]
                    reverseStop = True
                else:
                    potentialSecondDigit = getDigitFromLetterDigits(numDict, reverseString)
                    if (potentialSecondDigit is not None):
                        secondDigit = potentialSecondDigit
                        reverseStop = True

            if (reverseStop and forwardStop):
                break
        
        calibrationValue = int(firstDigit + secondDigit)
        sum += calibrationValue

    print(sum)

