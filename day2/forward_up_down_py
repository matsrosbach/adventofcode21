input = open("input_day2", "r")

splitInput = list(filter(lambda i: i != '', input.read().split("\n")))

horizontalPosition = 0
depth = 0

for inputLine in splitInput:
    command = inputLine.split(" ")[0]
    number = int(inputLine.split(" ")[1])
    
    if command.startswith('forward'):
        horizontalPosition += number
    elif command.startswith('down'):
        depth += number
    elif command.startswith('up'):
        depth -= number

print('The answer is:' + str(horizontalPosition * depth))


