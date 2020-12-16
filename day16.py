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
    invalidFields = {}
    validFields = {}
    for field in ticket:
        validFields[field] = []
        invalidFields[field] = []
        for rule in rules:
            if (fieldValidForRule(field, rule)):
                validFields[field].append(rule)
            else:
                invalidFields[field].append(rule)
    return (validFields, invalidFields)


def task1():
    invalidTickets = []
    i = 0
    for ticket in nearbyTickets:
        (valid, invalid) = validFields(ticket)
        for key in valid:
            if len(valid[key]) == 0:
                invalidTickets.append(key)
        i += 1
    return sum(invalidTickets)


def task2():
    # ['class', 'row', 'seat']
    ticketFields = [rule.split(":")[0] for rule in rules]
    # number of fields per ticket
    fieldLen = len(ticketFields)
    # {1: ['class, row']} means index 1 can be either class or row
    possibleFields = {}
    for i in range(fieldLen):
        possibleFields[i] = ticketFields
    # Go through each nearby ticket and update possibleField as we get more information
    for ticket in nearbyTickets:
        (valid, invalid) = validFields(ticket)
        # Check if ticket is invalid
        invalid = [len(val) == 0 for val in valid.values()]
        if any(invalid):
            continue
        # Go through fields a valid ticket
        i = 0
        for key in valid:
            fieldsInKey = [field.split(":")[0] for field in valid[key]]
            possibleFields[i] = list(
                filter(lambda x: x in fieldsInKey, possibleFields[i]))
            i += 1
    # sort after size
    sortedFields = sorted(possibleFields, key=lambda k: len(
        possibleFields[k]))
    # DEBUG
    for k in sortedFields:
        possibilities = possibleFields[k]
        if(len(possibilities) < 7):
            print(k, possibilities)
    return ""


print("Task 1: ", task1())
print("Task 2: ", task2())
