def parse_input(input):
    numbers, nl, boards = input.partition('\n')
    number_list = numbers.split(',')
    board_list, board = list(), list()
    for l in boards[1:].splitlines():
        if len(l) == 0:
            board_list.append(board)
            board = list()
        else:
            board.append([[int(n), 0] for n in l.split()])

    board_list.append(board)
    return map(lambda n: int(n), number_list), board_list


def mark_board(n, board):
    for row in board:
        for elem in row:
            if elem[0] == n:
                elem[1] = 1
                break


def check_bingo(board):
    check_row = check_column = 1
    for row in board:
        check_row = 1
        for elem in row:
            check_row &= elem[1]
        if check_row == 1:
            return row

    for column in range(len(board)):
        check_column = 1
        for row in board:
            check_column &= row[column][1]
        if check_column == 1:
            return [n[column] for n in board]

    return None


def sum_unmarked(board):
    sum = 0
    for row in board:
        for elem in row:
            if elem[1] == 0:
                sum += elem[0]

    return sum


def compute(input):
    numbers, boards = parse_input(input)

    for n in numbers:
        for board in boards:
            mark_board(n, board)
            win_seq = check_bingo(board)
            if win_seq != None:
                return sum_unmarked(board) * n
