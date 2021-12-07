inputFile = open("input7", "r")

input = [int(i) for i in inputFile.read().split(",")]

lowestIdx = None
lowestSum = None
currentSum = 0
for idx in range(0, len(input)):
    for element in input:
        currentSum += abs(element - idx)

    if (lowestSum == None or lowestSum > currentSum):
        lowestSum = currentSum
        lowestIdx = idx
        currentSum = 0

print('The answer is: ', lowestSum)


