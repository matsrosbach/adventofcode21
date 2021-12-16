def convert_all_elements_to_int(input_list):
    result = input_list
    for idx in range(0, len(input_list)):
        result[idx] = [int(i) for i in input_list[idx]]

    return result

def create_empty_visited(input):
    visited = [ [ False for y in range(len(input)) ] for x in range(len(input[0])) ]
    return visited

def at_the_end(input, x, y):
    return (x == (len(input) - 1)) and (y == (len(input[0]) - 1))

def try_every_path(input, visited, x, y, sum, smallest_sum):
    if visited[x][y]:
        return smallest_sum
    
    if sum > smallest_sum:
        return smallest_sum

    visited_copy = [[i for i in row] for row in visited]
    visited_copy[x][y] = True
    sum += input[x][y]

    if at_the_end(input, x, y):
        if sum < smallest_sum:
            smallest_sum = sum
        return smallest_sum

    if x > 0:
        smallest_sum = try_every_path(input, visited_copy, x-1, y, sum, smallest_sum)
    if x < (len(visited)-1):
        smallest_sum = try_every_path(input, visited_copy, x+1, y, sum, smallest_sum)
    if y > 0:
        smallest_sum = try_every_path(input, visited_copy, x, y-1, sum, smallest_sum)
    if y < (len(visited[x])-1):
        smallest_sum = try_every_path(input, visited_copy, x, y+1, sum, smallest_sum)

    return smallest_sum

inputFile = open("input15", "r")
input = convert_all_elements_to_int(inputFile.read().splitlines())
visited = create_empty_visited(input)
smallest_sum = try_every_path(input, visited, 0, 0, 0, 10000000000)
smallest_sum = smallest_sum - input[0][0] # Don't count the start

print("The answer is: ", smallest_sum)



