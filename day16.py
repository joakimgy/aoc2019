rules = ["class: 1-3 or 5-7", "row: 6-11 or 33-44", "seat: 13-40 or 45-50"]

nearbyTickets = [7,3,47, 40,4,50, 55,2,20, 38,6,12]

def parseRule(rule):
    key = rule.split(":")[0]
    (lowRange, highRange) = rule.split(":")[1].split(" or ")
    return key, lowRange, highRange
    
def parseRange(range):
    lower = int(range.split("-")[0])
    higher = int(range.split("-")[1])
    return (lower, higher)
    
def ticketValidForRule(ticket, rule):
    (key, lowRange, highRange) = parseRule(rule)
    (firstLow, firstHigh) = parseRange(lowRange)
    (secondLow, secondHigh) = parseRange(highRange)
    return (ticket >= firstLow and ticket <= firstHigh) or (ticket >= secondLow and ticket <= secondHigh)

def findValidTickets(tickets):
    invalidTickets = []
    for ticket in tickets:
        valid = []
        for rule in rules:
            valid.append(ticketValidForRule(ticket, rule))
        if not any(valid):
            invalidTickets.append(ticket)
    return invalidTickets
    
def task1():
    validTickets = findValidTickets(nearbyTickets)
    return sum(validTickets)
    
print("Task 1: ", task1())
