def read_input(input_file):
    input = open(input_file, "r").readlines()

    for i in range(0, len(input)):
        input[i] = input[i].rstrip()

    algorithm = input[0]
    input_image = input[2:]
    return algorithm, input_image

def create_starting_output(input_image, algorithm, lit):
    character = ""

    if lit and algorithm[0] == "#":
        character = "#"
    else:
        character = "."
    output_image = []
    input_width = len(input_image[0])
    empty_row = character * (input_width+4) # Add 2 to width on each side
    output_image.append(empty_row)
    output_image.append(empty_row)
    for row in input_image:
        output_row = character + character + row + character + character
        output_image.append(output_row)
    output_image.append(empty_row)
    output_image.append(empty_row)
    return output_image

def get_pixel_string(x, y, starting_output):
    string = starting_output[x-1][y-1] + starting_output[x-1][y] + starting_output[x-1][y+1]
    string += starting_output[x][y-1] + starting_output[x][y] + starting_output[x][y+1]
    string += starting_output[x+1][y-1] + starting_output[x+1][y] + starting_output[x+1][y+1]
    return string

def convert_pixel_string_to_number(pixel_string):
    binary = ""
    for c in pixel_string:
        if c == ".":
            binary += "0"
        else:
            binary += "1"
    return int(binary, 2)


def create_output(starting_output, algorithm):
    output = []
    for x in range(1, len(starting_output)-1):
        row = ""
        for y in range(1, len(starting_output[0])-1):
            pixel_string = get_pixel_string(x, y, starting_output)
            number = convert_pixel_string_to_number(pixel_string)
            row += algorithm[number]
        output.append(row)

    return output

def count_lit_pixels(image):
    lit_pixels = 0
    for row in image:
        for character in row:
            if character == "#":
                lit_pixels += 1
    return lit_pixels



algorithm, input_image = read_input("input20")
starting_output = create_starting_output(input_image, algorithm, False)
output = create_output(starting_output, algorithm)
for i in range(0, 50-1):
    starting_output = create_starting_output(output, algorithm, i % 2 == 0)
    output = create_output(starting_output, algorithm)

lit_pixels = count_lit_pixels(output)

print("The answer is: ", lit_pixels)
