def intersect(c, d):
    ((cx1, cx2), (cy1, cy2), (cz1, cz2), value) = c
    ((dx1, dx2), (dy1, dy2), (dz1, dz2), value) = d
    if not(cx1 <= dx2 and cx2 >= dx1):
        return False

    if not(cy1 <= dy2 and cy2 >= dy1):
        return False

    if not(cz1 <= dz2 and cz2 >= dz1):
        return False

    return True

def get_intersection(c, d):
    ((cx1, cx2), (cy1, cy2), (cz1, cz2), csign) = c
    ((dx1, dx2), (dy1, dy2), (dz1, dz2), dsign) = d
    min_x = max(cx1, dx1)
    max_x = min(cx2, dx2)

    min_y = max(cy1, dy1)
    max_y = min(cy2, dy2)

    min_z = max(cz1, dz1)
    max_z = min(cz2, dz2)

    sign = csign * dsign

    if csign == dsign:
        sign = -csign

    elif csign == 1 and dsign == -1:
        sign = 1

    return ((min_x, max_x), (min_y, max_y), (min_z, max_z), sign)


def calculate_result(cuboids):
    res = 0
    for c in cuboids:
        ((cx1, cx2), (cy1, cy2), (cz1, cz2), csign) = c
        res += ((cx2 - cx1 + 1) * (cy2 - cy1 + 1) * (cz2 - cz1 + 1)) * csign
    return res

def get_instructions(file):
    instructions = []
    for line in f.readlines():
        line = line.strip()

        state, ranges = line.split(' ')
        x_range, y_range, z_range = ranges.split(',')

        x_range = x_range.split('=')[1]
        min_x, max_x = x_range.split('..')
        min_x, max_x = int(min_x), int(max_x)

        y_range = y_range.split('=')[1]
        min_y, max_y = y_range.split('..')
        min_y, max_y = int(min_y), int(max_y)

        z_range = z_range.split('=')[1]
        min_z, max_z = z_range.split('..')
        min_z, max_z = int(min_z), int(max_z)

        instructions.append([state, (min_x, max_x), (min_y, max_y), (min_z, max_z)])
    return instructions


with open('input22') as f:
    instructions = get_instructions(f)

    cuboids = []

    for state, x_range, y_range, z_range in instructions:
        min_x, max_x = x_range
        min_y, max_y = y_range
        min_z, max_z = z_range

        current = (x_range, y_range, z_range, -1 if state == "off" else 1)
        intersections = []

        for cuboid in cuboids:
            if intersect(current, cuboid):
                intersection = get_intersection(current, cuboid)
                intersections.append(intersection)

        for intersection in intersections:
            cuboids.append(intersection)

        if state == 'on':
            cuboids.append(current)

    res = calculate_result(cuboids)


    print("The answer is: ", res)
