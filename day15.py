finalNumber = 2020
starting_number = [14,3,1,0,9,5.]
history = {}

for index in range(0,len(starting_number)):
    history[starting_number[index]] = [index+1]

last_number = 0
for index in range(len(starting_number)+1, finalNumber+1):
    if (last_number in history and len(history[last_number])) > 1:
        last_number = (index-1)-history[last_number][-2]
    else:
        last_number = 0
        
    if (last_number in history):
        history[last_number].append(index)
    else:
        history[last_number] = [index]
    if (index == finalNumber):
        print(last_number)
