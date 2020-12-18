filename = "day18input.txt"

with open(filename) as f:
    inputarray = [line.rstrip() for line in f]
    inputarray = [line.replace(" ", "") for line in inputarray]

def evaluate(expression):
    count = 0
    operator = "+"
    i = -1
    while (i +1 < len(expression)):
        i += 1
        val = expression[i]
        # Handle parenthesis
        if (val == "("):
            exp = expressionInParenthesis(expression[i:])
            if (operator == "+"):
                count += evaluate(exp)
            elif (operator == "-"):
                count -= evaluate(exp)
            elif (operator == "*"):
                count *= evaluate(exp)
            else: 
                print("Something went wrong with operators")
            i += len(exp)+1
            continue
        if (val == ")"):
            print("ERROR")
            break
        # Change operator
        if (val == "+" or val == "*" or val == "-"):
            operator = val
        # Update value
        else:
            val = int(val)
            if (operator == "+"):
                count += val
            elif (operator == "-"):
                count -= val
            elif (operator == "*"):
                count *= val
            else: 
                print("Something went wrong with operators")
    return count

def expressionInParenthesis(expression):
    noLeft = 1
    noRight = 0
    result = ""
    for i in range(1, len(expression)):
        val = expression[i]
        if (val == "("):
            noLeft += 1
        if (val == ")"):
            noRight += 1
        if (noLeft == noRight):
            return result
        result += val

def task1():
    count = 0
    for expression in inputarray:
        count += evaluate(expression)
    return count

def task2():
    return ""

print("Task 1: ", task1())
print("Task 2: ", task2())