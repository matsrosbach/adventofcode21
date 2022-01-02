def read_input(input_file):
    input = open(input_file, "r").readlines()

    for i in range(0, len(input)):
        input[i] = input[i].rstrip()

    return input

instructions = read_input("input22")
cubes = [[[0 for k in range(104)] for j in range(104)] for i in range(104)]

for instruction in instructions:
    value = 0
    if instruction.startswith("on"):
        value = 1
    else:
        value = 0


    x_range, y_range, z_range = [[int(p) for p in l[2:].split("..")] for l in instruction.split(" ")[1].split(",")]
    for x in range(x_range[0], x_range[1] + 1):
        if x_range[0] >= -50 and x_range[1] <= 50:
            for y in range(y_range[0], y_range[1] + 1):
                if y_range[0] >= -50 and y_range[1] <= 50:
                    for z in range(z_range[0], z_range[1] + 1):
                        if z_range[0] >= -50 and z_range[1] <= 50:
                            cubes[x][y][z] = value

count = 0
for x in range(0, len(cubes)):
    for y in range(0, len(cubes[x])):
        for z in range(0, len(cubes[y])):
            count += cubes[x][y][z]


print("The answer is: ", count)
