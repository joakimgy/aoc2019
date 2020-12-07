filename = "day7input.txt"

with open(filename) as f:
    inputarray = [line.rstrip() for line in f]


def getRules():
    ruleDict = {}
    for rule in inputarray:
        bag = rule.split(" bags contain ")[0]
        bagCanContain = rule.split(" bags contain ")[1]
        ruleDict[bag] = bagCanContain
    return ruleDict


def getBagContent(rules, bagColor):
    content = rules[bagColor]
    if (content == "no other bags."):
        return {}
    colorCapacityDict = {}
    for bag in content.split(", "):
        bagCapacity = bag.split(" ")[0]
        bagColor = (bag.split(" ")[1] + " " + bag.split(" ")[2])
        colorCapacityDict[bagColor] = bagCapacity
    return colorCapacityDict


def ruleContainsShinyGold(rules, bagColor):
    content = getBagContent(rules, bagColor)
    if ("shiny gold" in content):
        return True
    else:
        return False


def task1():
    rules = getRules()
    bagsWithShinyGold = 0
    for bagColor in rules:
        if (ruleContainsShinyGold(rules, bagColor)):
            bagsWithShinyGold += 1
            continue
        for subBagColor in getBagContent(rules, bagColor):
            if (ruleContainsShinyGold(rules, subBagColor)):
                print(bagColor, subBagColor)
                bagsWithShinyGold += 1
                break
    return bagsWithShinyGold
# gold in bagcontent?
# gold in bagconent of bagcontent?


def task2():
    return "No answer"


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
