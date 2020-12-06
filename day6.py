import string
filename = "day6input.txt"

with open(filename) as f:
    inputarray = [line.rstrip() for line in f]


def answersOfGroups():
    groupList = []
    group = []
    for line in inputarray:
        if (line == ""):
            groupList.append(group)
            group = []
        else:
            group.append(line)
    groupList.append(group)
    return groupList


def task1():
    totalYesAnswers = 0
    for groupAnswer in answersOfGroups():
        allGroupAnswers = [item for sublist in groupAnswer for item in sublist]
        yesAnswersOfGroup = 0
        for question in string.ascii_lowercase:
            if question in allGroupAnswers:
                yesAnswersOfGroup += 1
        totalYesAnswers += yesAnswersOfGroup
    return totalYesAnswers


def task2():
    totalAllYesAnswers = 0
    for group in answersOfGroups():
        allAnswerYes = 0
        for question in string.ascii_lowercase:
            if (all([question in person for person in group])):
                allAnswerYes += 1
        totalAllYesAnswers += allAnswerYes
    return totalAllYesAnswers


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
