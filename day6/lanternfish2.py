def create_initial_list(input_list):
    fish_birth_counter = []
    for idx in range(0, 9):
        fish_birth_counter.append(input_list.count(idx))

    return fish_birth_counter

def skip_one_day_ahead(fish_counter):
    new_counter = [0] * 9
    number_of_births = fish_counter[0]
    print(number_of_births)
    for idx in range(0, 8):
        new_counter[idx] = fish_counter[idx+1]

    new_counter[8] = number_of_births
    new_counter[6] += number_of_births
    return new_counter

inputFile = open("input6", "r")

input = [int(i) for i in inputFile.read().split(",")]

fish_birth_counter = create_initial_list(input)

current_counter = fish_birth_counter

for idx in range(0, 256):
    current_counter = skip_one_day_ahead(current_counter)

result = 0
for count in current_counter:
    result += count

print('The answer is: ', result)


