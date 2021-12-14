def get_pairs(input):
    pairs = {}
    for i in range (2, len(input)):
        pairs[input[i].split(" -> ")[0]] = input[i].split(" -> ")[1]

    return pairs

def get_initial_count(template):
    count = {}
    result = {}
    for i in range(1, len(template)):
        pair = "" + template[i-1] + template[i]
        if pair in count:
            count[pair] += 1
        else:
            count[pair] = 1

    for element in template:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return count, result

def perform_step(count, pairs, result_count):
    result = count.copy()
    for pair in count.keys():
        number_of_pairs = count[pair]
        pair_insertion = pairs[pair]
        if pair_insertion in result_count:
            result_count[pair_insertion] += number_of_pairs
        else:
            result_count[pair_insertion] = number_of_pairs
        new_pair_1 = "" + pair[0] + pair_insertion
        new_pair_2 = "" + pair_insertion + pair[1]
        if new_pair_1 in result:
            result[new_pair_1] += number_of_pairs
        else:
            result[new_pair_1] = number_of_pairs
        if new_pair_2 in result:
            result[new_pair_2] += number_of_pairs
        else:
            result[new_pair_2] = number_of_pairs
        result[pair] -= count[pair]

    return result


inputFile = open("input14", "r")
input = inputFile.read().splitlines()
template = input[0]
pairs = get_pairs(input)

count, result = get_initial_count(template)

for i in range(0, 40):
    count = perform_step(count, pairs, result)

largest = 0
smallest = 100000000000000
for element in result.keys():
    if result[element] > largest:
        largest = result[element]
    if result[element] < smallest:
        smallest = result[element]


print(largest)
print(smallest)
print("The answer is: ", largest-smallest)



