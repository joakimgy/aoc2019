filename = "day9input.txt"


with open(filename) as f:
    inputarray = [int(line.rstrip()) for line in f]


def isSumOfPreamble(expectedSum, preamble):
    for number in preamble:
        for number2 in preamble:
            if (number == number2):
                continue
            if (number+number2 == expectedSum):
                return True
    return False


def task1():
    preambleLength = 25
    preamble = inputarray[0:preambleLength]
    for number in inputarray[len(preamble):]:
        if (not isSumOfPreamble(number, preamble)):
            return number
        preamble = preamble[1:]
        preamble.append(number)
    return "Number not found"


def findContiguousSet(expectedSum, array):
    contiguousSet = array[0:2]
    for number in array[2:]:
        if (sum(contiguousSet) == expectedSum):
            return contiguousSet
        if (sum(contiguousSet) > expectedSum):
            return []
        contiguousSet.append(number)


def task2():
    invalidNumber = task1()
    for index in range(len(inputarray)):
        contiguousSet = findContiguousSet(invalidNumber, inputarray[index:])
        if (contiguousSet):
            return min(contiguousSet)+max(contiguousSet)
    return "No result"


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
