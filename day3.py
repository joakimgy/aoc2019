filename = "day3input.txt"

with open(filename) as f:
    inputarray = [line.rstrip() for line in f]


def treesInPath(stepsRight, stepsDown):
    segmentLength = len(inputarray[0])
    trees = 0
    stepsTaken = 0
    for row in inputarray[::stepsDown]:
        tile = row[(stepsTaken*stepsRight) % segmentLength]
        stepsTaken += 1
        if (tile == "#"):
            trees += 1
    return trees


def task1():
    return treesInPath(3, 1)


def task2():
    return treesInPath(1, 1) * treesInPath(3, 1) * treesInPath(5, 1) * treesInPath(7, 1) * treesInPath(1, 2)


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
