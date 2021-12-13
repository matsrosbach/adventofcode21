def find_size_of_paper(input):
    largest_x = 0
    largest_y = 0
    for row in input:
        if row == "":
            break
        if largest_x < int(row.split(",")[0]):
            largest_x = int(row.split(",")[0])
        if largest_y < int(row.split(",")[1]):
            largest_y = int(row.split(",")[1])
    return largest_x, largest_y

def create_paper(x, y):
    return [[False for h in range(x+1)] for w in range(y+1)]

def fill_dots(input, paper):
    result = paper.copy()
    for row in input:
        if row == "":
            break
        result[int(row.split(",")[1])][int(row.split(",")[0])] = True

    return result

def perform_fold(paper, fold):
    result = paper.copy()
    line = int(fold.split("=")[1])
    if fold.startswith("y"):
        x_top = line-1
        for x in range(line+1, len(result)):
            for y in range(0, len(result[x])):
                
                result[x_top][y] = result[x_top][y] or result[x][y]
            x_top -= 1

        result = result[:line]

    else:
        for x in range(0, len(result)):           
            y_right = line-1
            for y in range(line+1, len(result[0])):
                result[x][y_right] = result[x][y_right] or result[x][y]
                y_right -= 1

        for idx in range(0, len(result)):
            result[idx] = result[idx][:line]
    return result
            



inputFile = open("input13", "r")
input = inputFile.read().splitlines()

largest_x, largest_y = find_size_of_paper(input)
paper = create_paper(largest_x, largest_y)
paper_with_dots = fill_dots(input, paper)

folds = []
for row in input:
    if row.startswith("fold along"):
        folds.append(row.split(" along ")[1])

result = paper_with_dots
for fold in folds:
    result = perform_fold(result, fold)


count = 0
for row in result:
    for element in row:
        if element:
            count += 1

for row in result:
    row_string = ""
    for element in row:
        if element:
            row_string += "#"
        else:
            row_string += " "
    print(row_string)





