def find_patterns(unique_pattern):
    result = [None] * 10
    order = [None] * 7
    for pattern in unique_pattern:
        if (len(pattern) == 2): # Find 1
            result[1] = pattern
        if (len(pattern) == 3): # Find 7
            result[7] = pattern
        if (len(pattern) == 4): # Find 4
            result[4] = pattern
        if (len(pattern) == 7): # Find 8
            result[8] = pattern

    for pattern in unique_pattern:
        if (len(pattern) == 6):
            if not (all(item in pattern for item in result[1])): # Find 6
                result[6] = pattern
            elif not (all(item in pattern for item in result[4])): # Find 0
                result[0] = pattern
            else: # Find 9
                result[9] = pattern

    for pattern in unique_pattern:
        if (len(pattern) == 5):
            if (all(item in pattern for item in result[1])): # Find 3
                result[3] = pattern
            elif (all(item in result[6] for item in pattern)): # Find 5
                result[5] = pattern
            else: # Find 2
                result[2] = pattern

    return result

with open("input8") as f:
    input = f.read().splitlines()

unique_patterns = []
digit_output = []
for line in input:
    unique_patterns.append([s.strip() for s in line.split(" | ")[0].split(" ")])
    digit_output.append([s.strip() for s in line.split(" | ")[1].split(" ")])

sum = 0

for idx in range(0, len(digit_output)):
    patterns = find_patterns(unique_patterns[idx])
    number = ""
    for digit in digit_output[idx]:
        for pattern_idx in range(0, len(patterns)):
            if (len(digit) == len(patterns[pattern_idx])):
                if (all(item in digit for item in patterns[pattern_idx])):
                    number += str(pattern_idx)

    sum += int(number)


print('The answer is: ', sum)

