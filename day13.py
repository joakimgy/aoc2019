import math

filename = "day13input.txt"

with open(filename) as f:
    inputarray = [line.rstrip() for line in f]


def task1():
    earliestTimestamp = int(inputarray[0])
    ids = [int(bus) for bus in list(
        filter(lambda bus: bus != "x", inputarray[1].split(",")))]
    nextDeparture = {}  # key = bus, value = next departure
    for bus in ids:
        nextDeparture[bus] = bus - (earliestTimestamp % bus)

    nextBus = min(nextDeparture, key=nextDeparture.get)
    return nextBus * nextDeparture[nextBus]


def task2():
    buses = [(offset, int(bus)) for offset, bus in enumerate(inputarray[1].split(",")) if bus != "x"]
    print(buses)

    timestamp = 0
    earliestMatch = 1 
    for offset, bus in buses:
        while True:
            if (timestamp + offset) % bus == 0:
                break
            timestamp += earliestMatch
        earliestMatch *= bus
    return timestamp


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
