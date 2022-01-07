class Instruction:
    def __init__(self, command, arguments):
        self.command = command
        self.arguments = arguments

def read_input(input_file):
    input = open(input_file, "r").readlines()

    for i in range(0, len(input)):
        input[i] = input[i].rstrip()

    instructions = []
    for row in input:
        instruction = Instruction(row.split(" ")[0], row.split(" ")[1:])
        instructions.append(instruction)

    return instructions

def is_number(arg):
    return arg.lstrip("-").isnumeric()

def perform_instructions(instructions, arg):
    variables = {}
    curr_arg = 0
    for instruction in instructions:
        if instruction.command == "inp":
            variables[instruction.arguments[0]] = arg[curr_arg]
            curr_arg += 1
        if instruction.command == "add":
            variable_a = instruction.arguments[0]
            value_a = variables.get(variable_a, 0)
            if is_number(instruction.arguments[1]):
                value_b = int(instruction.arguments[1])
            else:
                variable_b = instruction.arguments[1]
                value_b = variables.get(variable_b, 0)
            variables[variable_a] = value_a + value_b
        if instruction.command == "mul":
            variable_a = instruction.arguments[0]
            value_a = variables.get(variable_a, 0)
            if is_number(instruction.arguments[1]):
                value_b = int(instruction.arguments[1])
            else:
                variable_b = instruction.arguments[1]
                value_b = variables.get(variable_b, 0)
            variables[variable_a] = value_a * value_b
        if instruction.command == "div":
            variable_a = instruction.arguments[0]
            value_a = variables.get(variable_a, 0)
            if is_number(instruction.arguments[1]):
                value_b = int(instruction.arguments[1])
            else:
                variable_b = instruction.arguments[1]
                value_b = variables.get(variable_b, 0)
            variables[variable_a] = value_a / value_b
        if instruction.command == "mod":
            variable_a = instruction.arguments[0]
            value_a = variables.get(variable_a, 0)
            if is_number(instruction.arguments[1]):
                value_b = int(instruction.arguments[1])
            else:
                variable_b = instruction.arguments[1]
                value_b = variables.get(variable_b, 0)
            variables[variable_a] = value_a % value_b
        if instruction.command == "eql":
            variable_a = instruction.arguments[0]
            value_a = variables.get(variable_a, 0)
            if is_number(instruction.arguments[1]):
                value_b = int(instruction.arguments[1])
            else:
                variable_b = instruction.arguments[1]
                value_b = variables.get(variable_b, 0)
            variables[variable_a] = 1 if value_a == value_b else 0

    print("x:", variables["x"], " y:", variables["y"], " z:", variables["z"], " w:", variables["w"])
    return variables["z"]

def contains_zero(number):
    return '0' in str(number)


instructions = read_input("small_input24")
highest = 0
#for number in range(11111111111111, 99999999999999 + 1):
#    if contains_zero(number):
#        continue
#    else:
#        print(number, " ", highest)
#        exit_code = perform_instructions(instructions, [int(a) for a in str(number)])
#        if exit_code == 0:
#            highest = number
#print(highest)

perform_instructions(instructions, [9])

print("The answer is: ", "?")
