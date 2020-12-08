import copy
filename = "day8input.txt"

with open(filename) as f:
    inputarray = [line.rstrip().split(" ") for line in f]


def runProgram(program):
    accumulator = 0
    index = 0
    visitedIndexes = []
    while (index not in visitedIndexes):
        if (index >= len(program)):
            return "Program finished running. Accumalator = " + str(accumulator)
        visitedIndexes.append(index)
        (cmd, value) = program[index]
        if (cmd == "acc"):
            accumulator += int(value)
        if (cmd == "jmp"):
            index += int(value)
            continue
        index += 1
    return "Program ran one loop. Accumulator = " + str(accumulator)


def task1():
    accumulator = runProgram(inputarray)
    return accumulator


def task2():
    for index in range(len(inputarray)):
        (cmd, value) = inputarray[index]
        program = copy.deepcopy(inputarray)
        if (cmd == "jmp"):
            program[index][0] = "nop"
        if (cmd == "nop"):
            program[index][0] = "jmp"
        output = runProgram(program)
        if ("Program finished" in output):
            return output
    return "No result"


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
