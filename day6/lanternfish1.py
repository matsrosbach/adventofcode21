class Lanternfish:
    def __init__(self, timer):
        self.timer = timer

def create_initial_list(input_list):
    fish_list = []
    for input in input_list:
        fish_list.append(Lanternfish(input))

    return fish_list

def skip_one_day_ahead(fish_list):
    for fish in fish_list:
        if (fish.timer == 0):
            fish_list.append(Lanternfish(9)) # Should've been 8, but the loop decreases it by one
            fish.timer = 6
        else:
            fish.timer -= 1

inputFile = open("input6", "r")

input = [int(i) for i in inputFile.read().split(",")]

fish_list = create_initial_list(input)

for idx in range(0, 80):
    skip_one_day_ahead(fish_list)

print('The answer is: ', len(fish_list))


