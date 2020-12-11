import copy
filename = "day11input.txt"

with open(filename) as f:
    inputarray = [list(line.rstrip()) for line in f]


def adjacentSeats(seatRow, seatCol, currentSeatings):
    adjacent = []
    for row in range(seatRow-1, seatRow+2):
        for col in range(seatCol-1, seatCol+2):
            if (row == seatRow and col == seatCol):
                continue
            if (row < 0 or row >= len(currentSeatings)):
                continue
            if (col < 0 or col >= len(currentSeatings[0])):
                continue
            adjacent.append(currentSeatings[row][col])
    return adjacent


def move(currentSeatings):
    newSeatings = copy.deepcopy(currentSeatings)
    for row in range(0, len(currentSeatings)):
        for col in range(0, len(currentSeatings[0])):
            currentSeat = currentSeatings[row][col]
            adjacent = adjacentSeats(row, col, currentSeatings)
            if (currentSeat == "."):
                newSeatings[row][col] = currentSeat
            elif (adjacent.count("#") == 0):
                newSeatings[row][col] = "#"
            elif (adjacent.count("#") >= 4):
                newSeatings[row][col] = "L"
            else:
                newSeatings[row][col] = currentSeat

    return newSeatings


def task1():
    currentSeatings = inputarray
    while (currentSeatings != move(currentSeatings)):
        currentSeatings = move(currentSeatings)

    stringWithAllSeats = "".join(["".join(row) for row in currentSeatings])
    return stringWithAllSeats.count("#")


def task2():
    return ""


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
