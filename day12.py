import copy
filename = "day12input.txt"

with open(filename) as f:
    inputarray = [line.rstrip() for line in f]


def task1():
    direction = 0  # east (north is 90, west is 180, south 270)
    coordinate = {"x": 0, "y": 0}
    for cmd in inputarray:
        if "N" in cmd:
            coordinate["y"] += int(cmd[1:])
        if "S" in cmd:
            coordinate["y"] -= int(cmd[1:])
        if "E" in cmd:
            coordinate["x"] += int(cmd[1:])
        if "W" in cmd:
            coordinate["x"] -= int(cmd[1:])
        if "L" in cmd:
            direction = (direction + int(cmd[1:])) % 360
        if "R" in cmd:
            direction = (direction - int(cmd[1:])) % 360
        if "F" in cmd:
            if (direction == 0):
                coordinate["x"] += int(cmd[1:])
            if (direction == 90):
                coordinate["y"] += int(cmd[1:])
            if (direction == 180):
                coordinate["x"] -= int(cmd[1:])
            if (direction == 270):
                coordinate["y"] -= int(cmd[1:])

    return abs(coordinate["x"]) + abs(coordinate["y"])


def task2():
    coordinateShip = {"x": 0, "y": 0}
    waypoint = {"x": 10, "y": 1}
    for cmd in inputarray:
        if "N" in cmd:
            waypoint["y"] += int(cmd[1:])
        if "S" in cmd:
            waypoint["y"] -= int(cmd[1:])
        if "E" in cmd:
            waypoint["x"] += int(cmd[1:])
        if "W" in cmd:
            waypoint["x"] -= int(cmd[1:])
        if "L" in cmd:
            rotation = int(cmd[1:])
            waypointX = waypoint["x"]
            waypointY = waypoint["y"]
            if rotation == 90:
                waypoint["x"] = -waypointY
                waypoint["y"] = waypointX
            if rotation == 180:
                waypoint["x"] = -waypointX
                waypoint["y"] = -waypointY
            if rotation == 270:
                waypoint["x"] = waypointY
                waypoint["y"] = -waypointX
        if "R" in cmd:
            rotation = int(cmd[1:])
            waypointX = waypoint["x"]
            waypointY = waypoint["y"]
            if rotation == 90:
                waypoint["x"] = waypointY
                waypoint["y"] = -waypointX
            if rotation == 180:
                waypoint["x"] = -waypointX
                waypoint["y"] = -waypointY
            if rotation == 270:
                waypoint["x"] = -waypointY
                waypoint["y"] = waypointX
        if "F" in cmd:
            coordinateShip["x"] += int(cmd[1:])*waypoint["x"]
            coordinateShip["y"] += int(cmd[1:])*waypoint["y"]

    return abs(coordinateShip["x"]) + abs(coordinateShip["y"])


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
