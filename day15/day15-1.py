file_path = 'day15.txt'

hashSum = 0

def getHashValue(word):
    hashValue = 0
    for char in word:
        hashValue += ord(char)
        hashValue *= 17
        hashValue %= 256
    return hashValue

with open(file_path, 'r') as file:
    wordArray = list(file.read().strip().split(","))
    # print(wordArray)
    
    for word in wordArray:
        hashSum += getHashValue(word)
    print (hashSum)


    