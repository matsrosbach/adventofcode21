input = open("input", "r")

splitInput = list(filter(lambda i: i != '', input.read().split("\n")))

counter = 0
previous = 0

for reading in splitInput:
    if int(reading) > previous:
        counter += 1
    previous = int(reading)

print('The answer is:' + str(counter-1))


