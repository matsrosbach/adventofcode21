def convert_all_elements_to_int(input_list):
    result = input_list
    for idx in range(0, len(input_list)):
        result[idx] = [int(i) for i in input_list[idx]]

    return result

def is_low_point(input, x, y):
    lowest_point = 9
    if x > 0:
        if (input[x-1][y] < lowest_point):
            lowest_point = input[x-1][y]
    if x < (len(input)-1):
        if (input[x+1][y] < lowest_point):
            lowest_point = input[x+1][y]
    if y > 0:
        if (input[x][y-1] < lowest_point):
            lowest_point = input[x][y-1]
    if y < (len(input[0])-1):
        if (input[x][y+1] < lowest_point):
            lowest_point = input[x][y+1]

    if (input[x][y] < lowest_point):
        return True
    else:
        return False

def compute_total_risk(input):
    total_risk = 0
    for x in range(0, len(input)):
        for y in range(0, len(input[x])):
            if (is_low_point(input, x, y)):
                total_risk += input[x][y] + 1

    return total_risk


with open("input9") as f:
    input = f.read().splitlines()

input = convert_all_elements_to_int(input)

result = compute_total_risk(input)

print('The answer is: ', result)

