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

def find_size_of_basin(input, x, y, checked, size):
    if input[x][y] != 9 and not checked[x][y]:
        size += 1
        checked[x][y] = True

    # Check up
    if x > 0:
        if not checked[x-1][y] and input[x-1][y] != 9:
            checked, size = find_size_of_basin(input, x-1, y, checked, size)
    if x < (len(input)-1):
        if not checked[x+1][y] and input[x+1][y] != 9:
            checked, size = find_size_of_basin(input, x+1, y, checked, size)
    if y > 0:
        if not checked[x][y-1] and input[x][y-1] != 9:
            checked, size = find_size_of_basin(input, x, y-1, checked, size)
    if y < (len(input[x])-1):
        if not checked[x][y+1] and input[x][y+1] != 9:
            checked, size = find_size_of_basin(input, x, y+1, checked, size)

    return checked, size


with open("input9") as f:
    input = f.read().splitlines()

input = convert_all_elements_to_int(input)
checked = [row[:] for row in input]
for x in range(0, len(checked)):
    for y in range(0, len(checked[x])):
        checked[x][y] = False

top1 = 0
top2 = 0
top3 = 0
for x in range(0, len(input)):
    for y in range(0, len(input[x])):
        if is_low_point(input, x, y):
            # Clear checked
            checked = [row[:] for row in input]
            for xx in range(0, len(checked)):
                for yy in range(0, len(checked[xx])):
                    checked[xx][yy] = False

            checked, size = find_size_of_basin(input, x, y, checked, 0)

            if size > top1:
                top3 = top2
                top2 = top1
                top1 = size
            elif size > top2:
                top3 = top2
                top2 = size
            elif size > top3:
                top3 = size

# Clear checked
checked = [row[:] for row in input]
for x in range(0, len(checked)):
    for y in range(0, len(checked[x])):
        checked[x][y] = False

print('The answer is: ', top1*top2*top3)

