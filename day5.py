filename = "day5input.txt"

with open(filename) as f:
    inputarray = [line.rstrip() for line in f]


def findRow(seatIndicator):
    length = 128
    lower = 0
    higher = 127
    indicator = seatIndicator[:-3]
    for letter in indicator:
        length = length / 2
        if letter == "F":
            higher = higher - length
        if letter == "B":
            lower = lower + length
    return lower


def findColumn(seatIndicator):
    length = 8
    lower = 0
    higher = 7
    indicator = seatIndicator[-3:]
    for letter in indicator:
        length = length / 2
        if letter == "L":
            higher = higher - length
        if letter == "R":
            lower = lower + length
    return lower


def listOfSeatIDs():
    seatIDs = []
    for seat in inputarray:
        row = findRow(seat)
        column = findColumn(seat)
        seatID = row * 8 + column
        seatIDs.append(seatID)
    return seatIDs


def task1():
    seatIDs = listOfSeatIDs()
    return max(seatIDs)


def task2():
    seatIDs = listOfSeatIDs()
    seatIDs.sort()
    for id in range(min(seatIDs), max(seatIDs)+1):
        if (id not in seatIDs):
            return id


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
