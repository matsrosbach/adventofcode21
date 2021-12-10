def get_score(character):
    if character == '}':
        return 1197
    if character == ')':
        return 3
    if character == ']':
        return 57
    if character == '>':
        return 25137

def is_opening_bracket(character):
    return (character == '(') or (character == '{') or (character == '<') or (character == '[')

def is_matching_char(opening_char, closing_char):
    if (opening_char == '(')  and (closing_char == ')'):
        return True
    if (opening_char == '[') and (closing_char == ']'):
        return True
    if (opening_char == '{') and (closing_char == '}'):
        return True
    if (opening_char == '<') and (closing_char == '>'):
        return True
    return False


with open("input10") as f:
    input = f.read().splitlines()

score = 0
for row in input:
    stack = []
    for char in row:
        if is_opening_bracket(char):
            stack.append(char)
        else:
            poppedChar = stack.pop()
            if not is_matching_char(poppedChar, char):
                score += get_score(char)
                break



print('The answer is: ', score)

