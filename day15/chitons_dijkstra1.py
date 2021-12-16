def convert_all_elements_to_int(input_list):
    result = input_list
    for idx in range(0, len(input_list)):
        result[idx] = [int(i) for i in input_list[idx]]

    return result

def create_initial_shortest_path(input):
    sp = [ [ 1000000000 for y in range(len(input)) ] for x in range(len(input[0])) ]
    sp[0][0] = 0
    return sp

def create_initial_visited(input):
    visited = [ [ False for y in range(len(input)) ] for x in range(len(input[0])) ]
    return visited

def at_the_end(input, x, y):
    return (x == (len(input) - 1)) and (y == (len(input[0]) - 1))

def find_smallest_index(shortest, visited):
    smallest = 1000000000
    sx = -1
    sy = -1
    for x in range(0, len(shortest)):
        for y in range(0, len(shortest[x])):
            if shortest[x][y] < smallest and not visited[x][y]:
                smallest = shortest[x][y]
                sx = x
                sy = y
    return sx, sy


def find_shortest_paths(input, shortest_path, visited):
    x = 0
    y = 0
    while x != -1:
        x, y = find_smallest_index(shortest_path, visited)
        if x == -1:
            return
        
        if x > 0:
            new_path = shortest_path[x][y] + input[x-1][y]
            old_path = shortest_path[x-1][y]
            if new_path < old_path:
                shortest_path[x-1][y] = new_path
        if x < (len(input)-1):
            new_path = shortest_path[x][y] + input[x+1][y]
            old_path = shortest_path[x+1][y]
            if new_path < old_path:
                shortest_path[x+1][y] = new_path
        if y > 0:
            new_path = shortest_path[x][y] + input[x][y-1]
            old_path = shortest_path[x][y-1]
            if new_path < old_path:
                shortest_path[x][y-1] = new_path
        if y < (len(input[x])-1):
            new_path = shortest_path[x][y] + input[x][y+1]
            old_path = shortest_path[x][y+1]
            if new_path < old_path:
                shortest_path[x][y+1] = new_path
    
        visited[x][y] = True
       


inputFile = open("input15", "r")
input = convert_all_elements_to_int(inputFile.read().splitlines())
shortest_paths = create_initial_shortest_path(input)
visited = create_initial_visited(input)
find_shortest_paths(input, shortest_paths, visited)

print("The answer is: ", shortest_paths[len(input)-1][len(input[0])-1])



