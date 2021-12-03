input = open("input", "r")

splitInput = list(filter(lambda i: i != '', input.read().split("\n")))
intInput = [int(i) for i in splitInput]

counter = 0
previousWindowSum = 0
windowSum = 0

for index, value in enumerate(splitInput):
    if index >= 2:
        windowSum = intInput[index-2] + intInput[index-1] + intInput[index];
        if windowSum > previousWindowSum:
            counter += 1
        previousWindowSum = windowSum

print('The answer is:' + str(counter-1))


