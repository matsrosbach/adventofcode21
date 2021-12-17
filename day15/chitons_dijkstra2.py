class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

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

def wrap_around(x):
    if x < 10:
        return x
    else:
        return (x%10)+1

def copy_input(input, big, x_tile, y_tile):
    for x in range(0, len(input)):
        for y in range(0, len(input[x])):
            big[x+(x_tile*len(input))][y+(y_tile*len(input[x]))] = wrap_around(input[x][y]+x_tile+y_tile)

def create_big_input(input):
    big = [ [0 for y in range(len(input)*5) ] for x in range(len(input[0])*5) ]
    for x in range(0, 5):
        for y in range(0, 5):
            copy_input(input, big, x, y)
    return big


def find_smallest_index(potential_next, shortest, visited):
    s= 10000000000
    s_node = None
    for node in potential_next:
        if shortest[node.x][node.y] < s and not visited[node.x][node.y]:
            s = shortest[node.x][node.y]
            s_node = node
    if s_node is None:
        return -1, -1
    else:
        return s_node.x, s_node.y


def find_shortest_paths(input, shortest_path, visited):
    potential_next = []
    potential_next.append(Node(0,0))
    x = 0
    y = 0
    while x != -1:
        x, y = find_smallest_index(potential_next, shortest_path, visited)
        if x == -1:
            return
        
        if x > 0:
            new_path = shortest_path[x][y] + input[x-1][y]
            old_path = shortest_path[x-1][y]
            if new_path < old_path:
                shortest_path[x-1][y] = new_path
                potential_next.append(Node(x-1, y))
        if x < (len(input)-1):
            new_path = shortest_path[x][y] + input[x+1][y]
            old_path = shortest_path[x+1][y]
            if new_path < old_path:
                shortest_path[x+1][y] = new_path
                potential_next.append(Node(x+1, y))
        if y > 0:
            new_path = shortest_path[x][y] + input[x][y-1]
            old_path = shortest_path[x][y-1]
            if new_path < old_path:
                shortest_path[x][y-1] = new_path
                potential_next.append(Node(x, y-1))
        if y < (len(input[x])-1):
            new_path = shortest_path[x][y] + input[x][y+1]
            old_path = shortest_path[x][y+1]
            if new_path < old_path:
                shortest_path[x][y+1] = new_path
                potential_next.append(Node(x, y+1))
    
        visited[x][y] = True
        potential_next.remove(Node(x, y))
       


inputFile = open("input15", "r")
input = convert_all_elements_to_int(inputFile.read().splitlines())
big_input = create_big_input(input)
shortest_paths = create_initial_shortest_path(big_input)
visited = create_initial_visited(big_input)
find_shortest_paths(big_input, shortest_paths, visited)

print("The answer is: ", shortest_paths[len(big_input)-1][len(big_input[0])-1])



