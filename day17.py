import copy

filename = "day17input.txt"
with open(filename) as f:
    inputarray = [line.rstrip() for line in f]

initialState = {}
for x in range(len(inputarray)):
    for y in range(len(inputarray[0])):
        if inputarray[x][y] == "#":
            initialState[(x, y, 0)] = "#"


def isActive(location, state):
    (x, y, z) = location
    return (x, y, z) in state


def adjacentCoordinates(coordinate):
    (x, y, z) = coordinate
    adjacent = []
    for xi in range(x-1, x+2):
        for yi in range(y-1, y+2):
            for zi in range(z-1, z+2):
                adjacent.append((xi, yi, zi))
    adjacent.remove((x, y, z))
    return adjacent


def activeNeighbors(coordinate, state):
    active = []
    for coord in adjacentCoordinates(coordinate):
        if isActive(coord, state):
            active.append(coord)
    return active


def move(state):
    nextState = copy.deepcopy(state)
    for coordinate in state:
        adjacent = activeNeighbors(coordinate, state)
        if not (len(adjacent) == 2 or len(adjacent) == 3):
            if coordinate in nextState:
                nextState.pop(coordinate)
        for coord in adjacentCoordinates(coordinate):
            active = isActive(coord, state)
            adjacent = activeNeighbors(coord, state)
            if active and not (len(adjacent) == 2 or len(adjacent) == 3):
                if coord in nextState:
                    nextState.pop(coord)
            if not active and len(adjacent) == 3:
                nextState[coord] = "#"
    return nextState


def task1():
    state = initialState
    for cycle in range(0, 6):
        state = move(state)
    return len(state)


print("Task 1:", task1())
