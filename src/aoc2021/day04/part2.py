from .part1 import parse_input, mark_board, check_bingo, sum_unmarked
import copy


def compute(input):
    numbers, boards = parse_input(input)

    for n in numbers:
        for board in boards:
            if board[0][0][1] == 2:
                continue
            mark_board(n, board)
            win_seq = check_bingo(board)
            if win_seq != None:
                last_win_board_snapshot = copy.deepcopy(board)
                last_win_num = n
                board[0][0][1] = 2

    return sum_unmarked(last_win_board_snapshot) * last_win_num
