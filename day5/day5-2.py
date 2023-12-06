file_path = 'day5.txt'

sum = 0


def getMapNumber(number, mapArray):
    for map in mapArray:
        sourceRange = (map[1], map[1] + map[2] -1)
        if (number >= sourceRange[0] and number <= sourceRange[1]):
            diff = number - map[1]
            return map[0] + diff
        else:
            pass
    return number

def getReverseMapRange(number, mapArray):
    for map in mapArray:
        sourceRange = (map[0], map[0] + map[2] -1)
        if (number >= sourceRange[0] and number <= sourceRange[1]):
            diff = number - map[0]
            return map[1] + diff
        else:
            pass
    return number

with open(file_path, 'r') as file:
    gardenDict = {}
    fileContent = file.read().strip().split("\n")
    # print(fileContent)

    # Prepare garden dictionary
    currentKey = None
    for line in fileContent:
        if line.endswith(':'):
            currentKey = line[:-1].strip()
            gardenDict[currentKey] = []
        elif "seeds:" in line:
            seedsArray = line.split(":")
            gardenDict[seedsArray[0]] = [int(value) for value in seedsArray[1].split()]
        elif line == '':
            pass
        else:
            values = [int(value) for value in line.split()]
            gardenDict[currentKey].append(values)

    locationArray = []

    # for i in range(0, len(gardenDict['seeds']), 2):
    #     startSeed = gardenDict['seeds'][i]
    #     endSeed = gardenDict['seeds'][i] + gardenDict['seeds'][i+1] -1

    #     for i in range(startSeed, endSeed+1, 1):
    # for seed in gardenDict['seeds']:
    #     mapArray = []

    #     soilNumber = getMapNumber(seed, gardenDict['seed-to-soil map'])
    #     fertiliserNumber = getMapNumber(soilNumber, gardenDict['soil-to-fertilizer map'])
    #     waterNumber = getMapNumber(fertiliserNumber, gardenDict['fertilizer-to-water map'])
    #     lightNumber = getMapNumber(waterNumber, gardenDict['water-to-light map'])
    #     tempNumber = getMapNumber(lightNumber, gardenDict['light-to-temperature map'])
    #     humidityNumber = getMapNumber(tempNumber, gardenDict['temperature-to-humidity map'])
    #     locationNumber = getMapNumber(humidityNumber, gardenDict['humidity-to-location map'])
    #     locationArray.append(locationNumber)


    testNumber = getReverseMapRange(3024237462, gardenDict['temperature-to-humidity map'])

    print(testNumber)


    # print(locationArray)
    # minLocationNumber = min(locationArray)
    # print(minLocationNumber)
    # print(gardenDict)

    
        
    

            

        