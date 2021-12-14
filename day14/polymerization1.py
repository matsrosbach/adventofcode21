def get_pairs(input):
    pairs = {}
    for i in range (2, len(input)):
        pairs[input[i].split(" -> ")[0]] = input[i].split(" -> ")[1]

    return pairs

def perform_step(template, pairs):
    result = [None] * (len(template) * 2 - 1)
    result_idx = 1
    result[0] = template[0]
    for i in range(1, len(template)):
        result[result_idx] = pairs["" + template[i-1] + template[i]]
        result[result_idx+1] = template[i]
        result_idx += 2
    return result
        

inputFile = open("input14", "r")
input = inputFile.read().splitlines()
template = input[0]
pairs = get_pairs(input)
result = template
for i in range(0, 10):
    result = perform_step(result, pairs)

count = {}
for element in result:
    if element in count:
        count[element] += 1
    else:
        count[element] = 1

largest = 0
smallest = 1000000
for element in count.keys():
    if count[element] > largest:
        largest = count[element]
    if count[element] < smallest:
        smallest = count[element]


print("The answer is: ", largest-smallest)



