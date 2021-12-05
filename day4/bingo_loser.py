def find_board(input, lineNumber):
    board = []
    for index in range (0, 5):
        board.append([int(item) for item in input[lineNumber + index].split()])

    return board

def find_all_boards(input):
    boards = []
    currentLineNumber = 2
    while currentLineNumber < (len(input) -1):
        boards.append(find_board(input, currentLineNumber))
        currentLineNumber += 6
    return boards

def exists_in_list(number, listToCheck):
    for element in listToCheck:
        if (number == element):
            return True

    return False

def check_row(row, pickedNumbers):
    for element in row:
        if not exists_in_list(element, pickedNumbers):
            return False
    return True

def check_rows(board, pickedNumbers):
#    print(board, pickedNumbers)
    for row in board:
        if check_row(row, pickedNumbers) == True:
            return True
    
    return False

def check_column(board, index, pickedNumbers):
    for row in range(0, len(board)):
        if not exists_in_list(board[row][index], pickedNumbers):
            return False
    return True


def check_columns(board, pickedNumbers):
    for column in range(0, len(board[0])):
        if check_column(board, column, pickedNumbers):
            return True

    return False

def find_next_winner(boards, numberOrder):
    pickedNumbers = []

    for number in numberOrder:
        pickedNumbers.append(number)
        for boardIndex in range(0, len(boards)):
            if (check_rows(boards[boardIndex], pickedNumbers) == True):
                return boards[boardIndex]
            if (check_columns(boards[boardIndex], pickedNumbers) == True):
                return boards[boardIndex]

def find_picked_numbers_to_win(board, numberOrder):
    pickedNumbers = []

    for number in numberOrder:
        pickedNumbers.append(number)
        if (check_rows(board, pickedNumbers) == True):
            return pickedNumbers
        if (check_columns(board, pickedNumbers) == True):
            return pickedNumbers


def calculate_score(board, numberOrder):
    pickedNumbers = find_picked_numbers_to_win(board, numberOrder)
    sum = 0
    for row in board:
        for element in row:
            if not (exists_in_list(element, pickedNumbers)):
                sum += element

    return sum * pickedNumbers[len(pickedNumbers)-1]

inputFile = open("input4", "r")

input = inputFile.read().splitlines()

numberOrder = [int(item) for item in input[0].split(",")]

boards = find_all_boards(input)

while len(boards) > 1:
    winnerBoardIndex = find_next_winner(boards, numberOrder)
    boards.remove(winnerBoardIndex)

score = calculate_score(boards[0], numberOrder)



print('The answer is: ', score)


