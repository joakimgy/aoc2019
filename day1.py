filename = "day1input.txt"

with open('day1input.txt') as f:
    inputarray = [int(line.rstrip()) for line in f]


def task1():
    for number1 in inputarray:
        for number2 in inputarray:
            sum = number1+number2
            if (sum == 2020):
                print("Task 1: ", number1*number2)
                return


def task2():
    for number1 in inputarray:
        for number2 in inputarray:
            for number3 in inputarray:
                sum = number1+number2+number3
                if (sum == 2020):
                    print("Task 2: ", number1*number2*number3)
                    return


task1()
task2()
