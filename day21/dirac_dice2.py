def read_input(input_file):
    input = open(input_file, "r").readlines()

    for i in range(0, len(input)):
        input[i] = input[i].rstrip()

    player_1 = int(input[0].split("position: ")[1])
    player_2 = int(input[1].split("position: ")[1])


    return [player_1, player_2]

init_positions = read_input("input21")
goal = 21
initial_state = (init_positions[0], init_positions[1], 0, 0)
wins = [0,0]
adds = [z+y+x for x in range(1,4) for y in range(1,4) for z in range(1,4)]
perms = {a:adds.count(a) for a in adds}
states = {(x,y,z,w):0 for x in range(1,11) for y in range(1,11) for z in range(0,goal) for w in range(0,goal)}
states[initial_state] = 1
while not max(states.values()) == 0:
    for state,value in states.items():
        if value > 0:
            for p,n in perms.items():
                for q,m in perms.items():
                    pos= [(state[0]+p-1)%10+1,(state[1]+q-1)%10+1]
                    new=tuple(pos+[state[2]+pos[0],state[3]+pos[1]])
                    if max(new[2:]) < goal:
                        states[new] += value*n*m
                    elif new[3] >= goal and new[2] < goal:
                        wins[1] += value*m*n
                if new[2] >= goal:
                    wins[0] += value*n
            states[state] = 0


print("The answer is: ", max([wins[0], wins[1]]))
