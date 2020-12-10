filename = "day10input.txt"

with open(filename) as f:
    inputarray = [int(line.rstrip()) for line in f]
inputarray.sort()
inputarray.insert(0, 0)
inputarray.append(max(inputarray)+3)


def task1():
    prevJolt = 0
    differences = {1: 0, 2: 0, 3: 0}
    for jolt in inputarray:
        diff = jolt - prevJolt
        if(diff == 0):
            continue
        differences[diff] += 1
        prevJolt = jolt
    return differences[1]*differences[3]


def adapterDictionary():
    adapterDictionary = {}
    for jolt in inputarray:
        adapterDictionary[jolt] = []

    for jolt in inputarray:
        for diff in range(1, 4):
            if jolt+diff in inputarray:
                adapterDictionary[jolt].append(diff)
        prevJolt = jolt

    return adapterDictionary


def distinctOrders(adapterDictionary):
    inputarray.reverse()
    countDict = {max(inputarray): 1}
    for jolt in inputarray[1:]:
        diffs = adapterDictionary[jolt]
        countDict[jolt] = sum([countDict[jolt+diff] for diff in diffs])
    return countDict[min(inputarray)]


def task2():
    adapterDict = adapterDictionary()
    return distinctOrders(adapterDict)


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
