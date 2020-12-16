filename = "day16input.txt"
rules = []
ticket = []
nearbyTickets = []
with open(filename) as f:
    inputarray = [line.rstrip() for line in f]
    i = 0
    inputArrays = {}
    for line in inputarray:
        if line == "":
            i += 1
            continue
        if (i == 0):
            rules.append(line)
        if (i == 1):
            ticket.append(line)
        if (i == 2):
            nearbyTickets.append(line)

nearbyTickets = [[int(ticket) for ticket in line.split(",")]
                 for line in nearbyTickets[1:]]


def parseRule(rule):
    key = rule.split(":")[0]
    (lowRange, highRange) = rule.split(":")[1].split(" or ")
    return key, lowRange, highRange


def parseRange(range):
    lower = int(range.split("-")[0])
    higher = int(range.split("-")[1])
    return (lower, higher)


def fieldValidForRule(ticket, rule):
    (key, lowRange, highRange) = parseRule(rule)
    (firstLow, firstHigh) = parseRange(lowRange)
    (secondLow, secondHigh) = parseRange(highRange)
    return (ticket >= firstLow and ticket <= firstHigh) or (ticket >= secondLow and ticket <= secondHigh)


def validFields(ticket):
    validFields = {}
    for field in ticket:
        validFields[field] = []
        for rule in rules:
            if (fieldValidForRule(field, rule)):
                validFields[field].append(rule)
    for key in validFields:
        validFields[key] = [field.split(":")[0] for field in validFields[key]]
    return validFields


def task1():
    invalidTickets = []
    i = 0
    for ticket in nearbyTickets:
        validFieldNames = validFields(ticket)
        for key in validFieldNames:
            if len(validFieldNames[key]) == 0:
                invalidTickets.append(key)
        i += 1
    return sum(invalidTickets)


def task2():
    ticketFields = [rule.split(":")[0] for rule in rules]
    fieldLen = len(ticketFields)
    remainingFields = {}
    for i in range(fieldLen):
        remainingFields[i] = ticketFields
    for ticket in nearbyTickets:
        validFieldNames = validFields(ticket)
        # Check if ticket is invalid
        invalidTicket = any(len(val) == 0 for val in validFieldNames.values())
        if invalidTicket:
            continue
        # Exclude some for certain indexes
        i = 0
        for okFields in validFieldNames.values():
            remainingFields[i] = list(
                filter(lambda x: x in okFields, remainingFields[i]))
            i += 1
    # sort after size
    sortedFields = sorted(remainingFields, key=lambda k: len(
        remainingFields[k]))
    # DEBUG
    for k in sortedFields:
        possibilities = remainingFields[k]
        if(len(possibilities) < 7):
            print(k, possibilities)
    return remainingFields


print("Task 1: ", task1())
print("Task 2: ", task2())
