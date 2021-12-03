input = open("input_day2", "r")

splitInput = list(filter(lambda i: i != '', input.read().split("\n")))

horizontalPosition = 0
depth = 0
aim = 0

for inputLine in splitInput:
    command = inputLine.split(" ")[0]
    number = int(inputLine.split(" ")[1])
    
    if command.startswith('forward'):
        horizontalPosition += number
        depth += (number * aim)
    elif command.startswith('down'):
        aim += number
    elif command.startswith('up'):
        aim -= number

print('The answer is:' + str(horizontalPosition * depth))


