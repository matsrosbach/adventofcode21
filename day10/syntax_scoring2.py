def get_score(character):
    if character == '{':
        return 3
    if character == '(':
        return 1
    if character == '[':
        return 2
    if character == '<':
        return 4

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

scores = []
for row in input:
    stack = []
    isCorrupted = False
    score = 0
    for char in row:
        if is_opening_bracket(char):
            stack.append(char)
        else:
            poppedChar = stack.pop()
            if not is_matching_char(poppedChar, char):
                isCorrupted = True
                break # Skip corrupted line

    if not isCorrupted:
        if len(stack) != 0:
            for i in range(0, len(stack)):
                score *= 5
                score += get_score(stack.pop())
            scores.append(score)


print('The answer is: ', sorted(scores)[len(scores)//2])

