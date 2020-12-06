filename = "day2input.txt"

with open(filename) as f:
    inputarray = [line.rstrip().split(" ") for line in f]


def task1():
    validCount = 0
    for element in inputarray:
        repetitions = element[0].split("-")
        min = int(repetitions[0])
        max = int(repetitions[1])
        letter = element[1][0]
        password = element[2]
        letterCount = password.count(letter)
        if (letterCount >= min and letterCount <= max):
            validCount += 1
    return validCount


def task2():
    validCount = 0
    for element in inputarray:
        repetitions = element[0].split("-")
        pos1 = int(repetitions[0])-1
        pos2 = int(repetitions[1])-1
        letter = element[1][0]
        password = element[2]
        if ((password[pos1] == letter) != (password[pos2] == letter)):
            validCount += 1
    return validCount


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
