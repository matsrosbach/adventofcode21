def read_input(input_file):
    input = open(input_file, "r").readlines()

    for i in range(0, len(input)):
        input[i] = input[i].rstrip()

    player_1 = int(input[0].split("position: ")[1])
    player_2 = int(input[1].split("position: ")[1])


    return [player_1, player_2]

def calculate_new_position(player, moves):
    rest = (player + moves) % 10
    if rest == 0:
        return 10
    else:
        return rest

def get_next_die_value(die):
    if die == 100:
        return 1
    else:
        return die + 1

players = read_input("input21")
scores = [0, 0]
die = 1
die_rolls = 0
current_player = 0

while scores[0] < 1000 and scores[1] < 1000:
    for i in range(0, 3):
        players[current_player] = calculate_new_position(players[current_player], die)
        die = get_next_die_value(die)
        die_rolls += 1
    scores[current_player] += players[current_player]
    current_player = 1 - current_player

print("The answer is: ", min(scores) * die_rolls)
