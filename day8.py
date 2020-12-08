filename = "day8input.txt"

with open(filename) as f:
    inputarray = [line.rstrip().split(" ") for line in f]


def task1():
    accumulator = 0
    index = 0
    visitedIndexes = []
    while (index not in visitedIndexes):
        visitedIndexes.append(index)
        (cmd, value) = inputarray[index]
        if (cmd == "acc"):
            accumulator += int(value)
        if (cmd == "jmp"):
            index += int(value)
            continue
        index += 1
    return accumulator


def task2():
    return "No answer"


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
