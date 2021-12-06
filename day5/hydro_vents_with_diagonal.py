class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def input_to_line(row):
    p1 = Point(int(row.split(" -> ")[0].split(",")[0]),int(row.split(" -> ")[0].split(",")[1]))
    p2 = Point(int(row.split(" -> ")[1].split(",")[0]),int(row.split(" -> ")[1].split(",")[1]))

    return Line(p1, p2)

def get_all_lines(input):
    lines = []
    for row in input:
        lines.append(input_to_line(row))
    return lines

def add_straight_lines(map, lines):
    for line in lines:
        if (line.p1.x == line.p2.x):
            if line.p1.y < line.p2.y:
                for yIndex in range(line.p1.y, line.p2.y+1, 1):
                    map[line.p1.x][yIndex] += 1
            else:
                for yIndex in range(line.p1.y, line.p2.y-1, -1):
                    map[line.p1.x][yIndex] += 1
        elif (line.p1.y == line.p2.y):
            if (line.p1.x < line.p2.x):
                for xIndex in range(line.p1.x, line.p2.x+1, 1):
                    map[xIndex][line.p1.y] += 1
            else:
                for xIndex in range(line.p1.x, line.p2.x-1,-1):
                    map[xIndex][line.p1.y] += 1
    return map


def add_diagonal_lines(map, lines):
    for line in lines:
        if abs((line.p1.x - line.p2.x)) == abs((line.p1.y - line.p2.y)):
            distance = line.p1.x - line.p2.x if line.p1.x > line.p2.x else line.p2.x - line.p1.x
            for i in range(0, distance+1):
                x = line.p1.x + i if line.p1.x < line.p2.x else line.p1.x - i
                y = line.p1.y + i if line.p1.y < line.p2.y else line.p1.y - i
                map[x][y] += 1
    return map
            



def create_map(lines):
    map = [[0 for c in range(1000)] for r in range(1000)]
    mapWithStraightLines = add_straight_lines(map, lines)
    completeMap = add_diagonal_lines(mapWithStraightLines, lines)
    return completeMap

inputFile = open("input5", "r")

input = inputFile.read().splitlines()

lines = get_all_lines(input)

map = create_map(lines)

counter = 0
for row in map:
    for element in row:
        if element > 1:
            counter += 1

print('The answer is: ', counter)


