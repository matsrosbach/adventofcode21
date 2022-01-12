def read_input(input_file):
    input = open(input_file, "r").readlines()

    for i in range(0, len(input)):
        input[i] = input[i].rstrip()
        input[i] = [*input[i]]

    return [*input]


def step(input):
    stuck = True
    map_after_east = [row[:] for row in input]
    for row in range(0, len(input)):
        for col in range(0, len(input[row])):
            if input[row][col] == ">":
                if input[row][(col+1) % len(input[row])] == ".":
                    map_after_east[row][col] = "."
                    map_after_east[row][(col+1) % len(input[row])] = ">"
                    stuck = False

    map_after_down = [row[:] for row in map_after_east]
    for row in range(0, len(map_after_east)):
        for col in range(0, len(map_after_east[row])):
            if map_after_east[row][col] == "v":
                if map_after_east[(row+1) % len(map_after_east)][col] == ".":
                    map_after_down[row][col] = "."
                    map_after_down[(row+1) % len(map_after_east)][col] = "v"
                    stuck = False

    return map_after_down, stuck


input = read_input("input25")
cucumber_map = input
stuck = False
steps = 0
while not stuck:
    cucumber_map, stuck = step(cucumber_map)
    steps += 1



print("The answer is: ", steps)
