file_path = 'day19.txt'

def prepareRulesAndRatings(file):
    rules = {}
    ratings = []

    isRuleCompleted = False
    for line in file:
        if (len(line.strip()) == 0):
            isRuleCompleted = True
            continue
        if (not isRuleCompleted):
            keyValue = line.strip().replace("}","").split("{")
            rules[keyValue[0]] = keyValue[1].split(",")
        else:
            rawRatings = line.strip().replace("{", "").replace("}", "").split(",")
            rating = {}
            for rawRating in rawRatings:
                keyValueRating = rawRating.split("=")
                rating[keyValueRating[0]] = int(keyValueRating[1])
            ratings.append(rating)
    return rules, ratings

def processWorkflow(workflow, rules, rating):
    while (True):
        rule = rules[workflow]
        for condition in rule:
            if (":" not in condition):
                workflow = condition
            else:
                conditionMapping = condition.split(":")
                dest = conditionMapping[1]
                destCondition = conditionMapping[0]
                if (">" in destCondition):
                    destConditionPart = destCondition.split(">")
                    conditionRating = destConditionPart[0]
                    conditionRatingValue = int(destConditionPart[1])
                    if (rating[conditionRating] > conditionRatingValue):
                        workflow = dest
                        break
                elif ("<" in destCondition):
                    destConditionPart = destCondition.split("<")
                    conditionRating = destConditionPart[0]
                    conditionRatingValue = int(destConditionPart[1])
                    if (rating[conditionRating] < conditionRatingValue):
                        workflow = dest
                        break
        
        if (workflow == "R" or workflow == "A"):
            break
    return workflow

def sumRating(rating):
    return sum(rating.values())

with open(file_path, 'r') as file:
    
    # Rules: {"px": ["a<2006:qkq", "m>2090:A", "rfg"], ...}
    # Ratings: [{"x": 787, "m": 2655, "a": 1222, "s": 2876}, {...}]
    rules, ratings = prepareRulesAndRatings(file)
    totalRating = 0

    for rating in ratings:
        workflow = "in"
        workflow = processWorkflow(workflow, rules, rating)
        if (workflow == "A"):
            totalRating += sumRating(rating)
    print(totalRating)
