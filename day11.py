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


def adjacentSeatsGeneric(seatRow, seatCol, currentSeatings):
    adjacent = {"n": [], "ne": [], "e": [], "se": [],
                "s": [], "sw": [], "w": [], "nw": []}
    noRows = len(currentSeatings)
    noCols = len(currentSeatings[0])
    # north
    for steps in range(seatRow-1, -1, -1):
        adjacent["n"].append(currentSeatings[steps][seatCol])
    # south
    for steps in range(seatRow+1, noRows):
        adjacent["s"].append(currentSeatings[steps][seatCol])
    # east
    for steps in range(seatCol+1, noCols):
        adjacent["e"].append(currentSeatings[seatRow][steps])
    # west
    for steps in range(seatCol-1, -1, -1):
        adjacent["w"].append(currentSeatings[seatRow][steps])
    # northeast
    for steps in range(1, min(noCols-seatCol, seatRow+1)):
        adjacent["ne"].append(
            currentSeatings[seatRow-steps][seatCol+steps])
    # southwest ## FEL
    for steps in range(1, min(seatCol+1, noRows-seatRow)):
        adjacent["sw"].append(
            currentSeatings[seatRow+steps][seatCol-steps])
    # northwest
    for steps in range(1, min(seatCol, seatRow)+1):
        adjacent["nw"].append(
            currentSeatings[seatRow-steps][seatCol-steps])
    # southeast
    for steps in range(1, min(noCols-seatCol, noRows-seatRow)):
        adjacent["se"].append(
            currentSeatings[seatRow+steps][seatCol+steps])
    cnt = 0
    for key in adjacent:
        for seat in adjacent[key]:
            if seat == "L":
                break
            if seat == "#":
                cnt += 1
                break
    return cnt


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


def moveTask2(currentSeatings):
    newSeatings = copy.deepcopy(currentSeatings)
    for row in range(0, len(currentSeatings)):
        for col in range(0, len(currentSeatings[0])):
            currentSeat = currentSeatings[row][col]
            adjacent = adjacentSeatsGeneric(row, col, currentSeatings)
            if (currentSeat == "."):
                newSeatings[row][col] = currentSeat
            elif (adjacent == 0):
                newSeatings[row][col] = "#"
            elif (adjacent >= 5):
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
    currentSeatings = inputarray
    while (currentSeatings != moveTask2(currentSeatings)):
        currentSeatings = moveTask2(currentSeatings)
    stringWithAllSeats = "".join(["".join(row) for row in currentSeatings])
    return stringWithAllSeats.count("#")


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
