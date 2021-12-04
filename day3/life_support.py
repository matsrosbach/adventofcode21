def find_most_common_value(input, index):
    counter = 0
    for line in input:
        if line[index] == '1':
            counter += 1
        else:
            counter -= 1

    if counter >= 0:
        return 1
    else:
        return 0

def find_least_common_value(input, index):
    mostCommon = find_most_common_value(input, index)
    if mostCommon == 0:
        return 1
    else:
        return 0

def filter_lines(input, index, bitCriteria):
    result = []
    for line in input:
        if int(line[index]) == bitCriteria:
            result.append(line)

    return result
    
def find_oxygen_rating(input):
    remainingInput = input
    for index in range(0, len(input[0])):
        if len(remainingInput) == 1:
            break
        else:
            remainingInput = filter_lines(remainingInput, index, find_most_common_value(remainingInput, index))
    
    return int(remainingInput[0], 2)


def find_co2_rating(input):
    remainingInput = input
    for index in range(0, len(input[0])):
        if len(remainingInput) == 1:
            break
        else:
            remainingInput = filter_lines(remainingInput, index, find_least_common_value(remainingInput, index))
    
    return int(remainingInput[0], 2)



inputFile = open("input3", "r")

input = inputFile.read().splitlines()

oxygenRating = find_oxygen_rating(input)
co2Rating = find_co2_rating(input)

print('The answer is: ', str(oxygenRating * co2Rating))


