from collections import deque as queue
import copy

file_path = 'day19.txt'

class Rating:
    def __init__(self, _xmas, _dest) -> None:
        self.xmas = _xmas
        self.dest = _dest

    def __str__(self) -> str:
        return "X: {0}, M: {1}, A: {2}, S: {3}".format(self.xmas['x'], self.xmas['m'], self.xmas['a'], self.xmas['s'])

class RatingRange:
    def __init__(self, _min, _max) -> None:
        self.min = _min
        self.max = _max

    def __str__(self) -> str:
        return "min: {0}, max: {1}".format(self.min, self.max)

def prepareRules(file):
    rules = {}
    for line in file:
        if (len(line.strip()) == 0):
            break
        keyValue = line.strip().replace("}","").split("{")
        rules[keyValue[0]] = keyValue[1].split(",")
    return rules

def getAllAcceptedRatingRange(ratingQueue, ratingValue, rules):
    acceptedRatingArray = []
    while(len(ratingQueue) > 0):
        rating: Rating = ratingQueue.popleft()

        # Check dest (R / A), assign to array and continue
        if (rating.dest == "A"):
            acceptedRatingArray.append(rating)
            continue
        if (rating.dest == "R"):
            continue

        ratingValue = rating.xmas
        rule = rules[rating.dest]
        for condition in rule:
            if (":" not in condition):
                newRating = Rating(ratingValue, condition)
                ratingQueue.append(newRating)
            
            else:
                conditionMapping = condition.split(":")
                dest = conditionMapping[1]
                destCondition = conditionMapping[0]
                if (">" in destCondition):
                    destConditionPart = destCondition.split(">")
                    conditionRating = destConditionPart[0]
                    conditionRatingValue = int(destConditionPart[1])
                    
                    newRatingValue = copy.deepcopy(ratingValue)
                    newRatingRange: RatingRange = newRatingValue[conditionRating]
                    newRatingRange.min = conditionRatingValue + 1
                    newRatingValue[conditionRating] = newRatingRange
                    newRating = Rating(newRatingValue, dest)
                    ratingQueue.append(newRating)

                    nextRatingRange: RatingRange = ratingValue[conditionRating]
                    nextRatingRange.max = conditionRatingValue
                    ratingValue[conditionRating] = nextRatingRange

                elif ("<" in destCondition):
                    destConditionPart = destCondition.split("<")
                    conditionRating = destConditionPart[0]
                    conditionRatingValue = int(destConditionPart[1])

                    newRatingValue = copy.deepcopy(ratingValue)
                    newRatingRange: RatingRange = newRatingValue[conditionRating]
                    newRatingRange.max = conditionRatingValue - 1
                    newRatingValue[conditionRating] = newRatingRange
                    newRating = Rating(newRatingValue, dest)
                    ratingQueue.append(newRating)

                    nextRatingRange: RatingRange = ratingValue[conditionRating]
                    nextRatingRange.min = conditionRatingValue
                    ratingValue[conditionRating] = nextRatingRange
    return acceptedRatingArray

def getTotalCombination(acceptedRatingArray):
    totalCombination = 0
    for acceptedRating in acceptedRatingArray:
        xRating = acceptedRating.xmas['x'].max - acceptedRating.xmas['x'].min + 1
        mRating = acceptedRating.xmas['m'].max - acceptedRating.xmas['m'].min + 1
        aRating = acceptedRating.xmas['a'].max - acceptedRating.xmas['a'].min + 1
        sRating = acceptedRating.xmas['s'].max - acceptedRating.xmas['s'].min + 1

        combinations = xRating * mRating * aRating * sRating
        totalCombination += combinations
    return totalCombination

with open(file_path, 'r') as file:
    
    # Rules: {"px": ["a<2006:qkq", "m>2090:A", "rfg"], ...}
    rules = prepareRules(file)

    ratingQueue = queue()
    ratingValue = {"x": RatingRange(1, 4000), "m": RatingRange(1, 4000), "a": RatingRange(1, 4000), "s": RatingRange(1, 4000)}
    initialRating = Rating(ratingValue, "in")
    ratingQueue.append(initialRating)

    acceptedRatingArray = getAllAcceptedRatingRange(ratingQueue, ratingValue, rules)
    totalCombination = getTotalCombination(acceptedRatingArray)

    print(totalCombination)
