inputFile = open("input3", "r")

input = inputFile.readlines()

gammaRateBinary = ''
epsilonRateBinary = ''

counter = [0 for i in range(len(input[0])-1)] #-1 to ignore the newline

for inputLine in input:
    for index in range(0, len(inputLine)-1): #-1 to ignore the newline
        if inputLine[index] == '0':
            counter[index] -= 1
        else:
            counter[index] += 1

for element in counter:
    if element > 0:
        gammaRateBinary += '1'
        epsilonRateBinary += '0'
    else:
        gammaRateBinary += '0'
        epsilonRateBinary += '1'

print('The answer is:' + str(int(gammaRateBinary, 2) * int(epsilonRateBinary, 2)))


