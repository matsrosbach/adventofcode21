def convert_all_elements_to_int(input_list):
    result = input_list
    for idx in range(0, len(input_list)):
        result[idx] = [int(i) for i in input_list[idx]]

    return result

def create_flashed_map(energy_map):
    flashed_map = [row[:] for row in energy_map]
    for x in range(0, len(flashed_map)):
        for y in range(0, len(flashed_map[x])):
            flashed_map[x][y] = False

    return flashed_map

def increase_energy(energy_map, flashed_map, x, y):
    energy_map[x][y] += 1
    perform_flash(energy_map, flashed_map, x, y)
    return energy_map, flashed_map

# Does not flash if it has already flashed
def perform_flash(energy_map, flashed_map, x, y):
    if flashed_map[x][y] or energy_map[x][y] <= 9:
        return
    flashed_map[x][y] = True
    if x > 0:
        if y > 0:
            increase_energy(energy_map, flashed_map, x-1, y-1)
        increase_energy(energy_map, flashed_map, x-1, y)
        if y < (len(energy_map[x]) - 1):
            increase_energy(energy_map, flashed_map, x-1, y+1)
    if y > 0:
        increase_energy(energy_map, flashed_map, x, y-1)
    if y < (len(energy_map[x]) - 1):
        increase_energy(energy_map, flashed_map, x, y+1)
    if x < (len(energy_map) - 1):
        if y > 0:
            increase_energy(energy_map, flashed_map, x+1, y-1)
        increase_energy(energy_map, flashed_map, x+1, y)
        if y < (len(energy_map[x]) - 1 ):
            increase_energy(energy_map, flashed_map, x+1, y+1)

    return energy_map, flashed_map



def perform_step(energy_map):
    flashed_map = create_flashed_map(energy_map)
    flashes = 0
    for x in range(0, len(energy_map)):
        for y in range(0, len(energy_map[x])):
            increase_energy(energy_map, flashed_map, x, y)

    for x in range(0, len(energy_map)):
        for y in range(0, len(energy_map[x])):
            if flashed_map[x][y]:
                energy_map[x][y] = 0
                flashes += 1

    if flashes == 100:
        return True
    else:
        return False




with open("input11") as f:
    input = f.read().splitlines()

flashes = 0
energy_map = convert_all_elements_to_int(input)
synced = False
steps = 0
while not synced:
    synced = perform_step(energy_map)
    steps += 1

print('The answer is: ', steps)

