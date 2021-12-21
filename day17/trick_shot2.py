# Input: target area: x=169..206, y=-108..-68
min_x = 169
max_x = 206
min_y = -108
max_y = -68


def is_within(x, y):
    if x >= min_x and x <= max_x and y >= min_y and y <= max_y:
        return True
    else:
        return False


def hits(init_x, init_y):
    x = 0
    y = 0
    vx = init_x
    vy = init_y
    while True:
        if is_within(x, y):
            return True
        if x > max_x:
            return False
        if x < min_x and vx == 0:
            return False
        if y < min_y:
            return False
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        vy -= 1

sum = 0
for x in range(0, max_x + 1):
    for y in range(min_y, abs(min_y) + 1):
        if hits(x, y):
            sum += 1

print("The answer is: ", sum)



