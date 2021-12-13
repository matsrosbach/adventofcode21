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
        x_top = 0
        for x in range(len(paper)-1, line, -1):
            for y in range(0, len(paper[x])):
                result[x_top][y] = paper[x_top][y] or paper[x][y]
            x_top += 1

        result = result[:line]

    else:
        for x in range(0, len(paper)):           
            y_left = 0
            for y in range(len(paper[0])-1, line, -1):
     #           print("x: ", x, ", y:", y, ", y_left:", y_left)
                result[x][y_left] = paper[x][y_left] or paper[x][y]
                y_left += 1

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

result = perform_fold(paper_with_dots, folds[0])
dots = 0
for row in result:
    for element in row:
        if element:
            dots += 1


print("The answer is: ", dots)



