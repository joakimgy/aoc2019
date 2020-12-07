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


rules = getRules()


def getBagContent(bagColor):
    content = rules[bagColor]
    if (content == "no other bags."):
        return {}
    colorCapacityDict = {}
    for bag in content.split(", "):
        bagCapacity = bag.split(" ")[0]
        bagColor = (bag.split(" ")[1] + " " + bag.split(" ")[2])
        colorCapacityDict[bagColor] = bagCapacity
    return colorCapacityDict


def bagContainsShinyGold(emptyBags, remainingBags):
    if (not remainingBags):
        return False
    stillEmpty = []
    stillRemaining = []
    for bag in remainingBags:
        if "shiny gold" in getBagContent(bag):
            return True
        if all([b in emptyBags for b in getBagContent(bag)]):
            continue
        for content in getBagContent(bag):
            if content in emptyBags:
                stillEmpty.append(content)
            else:
                stillRemaining.append(content)
    return bagContainsShinyGold(stillEmpty, stillRemaining)


def task1():
    emptyBags = list(filter(lambda bag: getBagContent(bag) == {}, rules))
    remainingBags = list(
        filter(lambda bag: bag not in (emptyBags+["shiny gold"]), rules))

    count = 0
    for bag in remainingBags:
        if (bagContainsShinyGold(emptyBags, [bag])):
            count += 1
    return count


def numberOfBagsInBag(emptyBags, bag):
    count = 1
    if (bag in emptyBags):
        return 1
    for content in getBagContent(bag):
        size = int(getBagContent(bag)[content])
        count += size * numberOfBagsInBag(emptyBags, content)
    return count


def task2():
    emptyBags = list(filter(lambda bag: getBagContent(bag) == {}, rules))
    count = numberOfBagsInBag(emptyBags, "shiny gold")
    return count - 1


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
