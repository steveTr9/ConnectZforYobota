import numpy as np
import sys


def check_slot(column_selection,board):
    # Check the available slot for the next piece
    for i in range(board.shape[0]):
        if board[board.shape[0] - 1 - i][column_selection] == 0:
            return board.shape[0] - 1 - i


def s_int(number):
    # Special s_int to deal with null variables and invalid variables
    try:
        if number != '':
            ans = int(number)
        else:
            ans = -1
        return ans
    except ValueError:
        print('8')
        sys.exit()


def read_file(path):
    # Checking file
    try:
        file = open(path)
        return file
    except Exception:
        print('9')
        sys.exit()


def parse_first_row_input(f):
    # Create an array of input data and checking for the data's format
    try:
        numbers = f.readline()
        numbers = numbers.split()
        if numbers:
            first_row_input = [int(i) for i in numbers]
            return first_row_input
    except ValueError:
        print('8')
        sys.exit()


def check_win_h(count, board, last_move_player, last_move_col, last_move_row, Win):
    # Check win horizontally
    if count+1 >= 2*Win:
        for k in range(Win):
            if (last_move_col - (Win-(k+1))) >= 0 and (last_move_col + k+1) <= board.shape[1]:
                if all( board[last_move_row,last_move_col - (Win-(k+1)):last_move_col + k+1] == last_move_player ):
                    return last_move_player


def check_win_v(count, board, last_move_player, last_move_col, last_move_row, Win):
    # Check win vertically
    if count+1 >= 2*Win:
        if (last_move_row + Win) <= board.shape[0]:
            if all(board[last_move_row : (last_move_row + Win),last_move_col] == last_move_player):
                return last_move_player


def check_win_nwse(count, board, last_move_player, last_move_col, last_move_row, Win):
    # Check win North West to South East
    # The logic behind:
    # the function scans all 'win' by 'win' matrices that containing the last_move in their diagonals
    # then, compare the diagonals to the player number in order to deduce the results
    if count+1 >= 2*Win:
        for k in range(Win):
            if ((last_move_row - (Win-(k+1))) >= 0 and (last_move_row + k+1) <= board.shape[0]
                    and (last_move_col - (Win-(k+1))) >= 0 and (last_move_col + k+1) <= board.shape[1]):
                targeted_matrix_nwse = (board[last_move_row - (Win-(k+1)):last_move_row + k+1,
                                   last_move_col - (Win-(k+1)):last_move_col + k+1])
                if (all(targeted_matrix_nwse.diagonal() == last_move_player)):
                    return last_move_player


def check_win_swne(count, board, last_move_player, last_move_col, last_move_row, Win):
    # Check win South West to North East
    # The logic behind:
    # the function scans all 'win' by 'win' matrices that containing the last_move in their 'flipped' diagonals
    # then, compare the 'flipped' diagonals to the player number in order to deduce the results
    if count+1 >= 2*Win:
        for k in range(Win):
            if ((last_move_row - (Win - (k + 1))) >= 0 and (last_move_row + k + 1) <= board.shape[0]
                    and (last_move_col - k) >= 0 and (last_move_col + (Win-k)) <= board.shape[1]):
                targeted_matrix_swne = np.fliplr(board[last_move_row - (Win - (k + 1)):last_move_row + k + 1,
                                                 last_move_col - (k): last_move_col + (Win - (k))])
                if  (all(targeted_matrix_swne.diagonal() == last_move_player)):
                    return last_move_player


def check_win(count, board, last_move_player, last_move_col, last_move_row, Win):
    win_h = check_win_h(count, board, last_move_player, last_move_col, last_move_row, Win)
    if win_h:
        return win_h
    win_v = check_win_v(count, board, last_move_player, last_move_col, last_move_row, Win)
    if win_v:
        return win_v
    win_nwse = check_win_nwse(count, board, last_move_player, last_move_col, last_move_row, Win)
    if win_nwse:
        return win_nwse
    win_swne = check_win_swne(count, board, last_move_player, last_move_col, last_move_row, Win)
    if win_swne:
        return win_swne


def check_end(count, Column, Row, result):
    if input_col == -1 and count - 1 < Column * Row and result == []:  # Conditions for the incomplete game
        return 3
    elif input_col == -1 and count - 1 == Column * Row and result == []:  # Conditions for the draw game
        return 0


if __name__ == '__main__':

    if len(sys.argv) == 1:
        data_file_path = input('Provide one input file: ')
    else:
        data_file_path = sys.argv[1]

    # Read file
    f = read_file( data_file_path )
    first_row_input = parse_first_row_input(f)

    # Define initial variables
    column = first_row_input[0]
    row = first_row_input[1]
    win = first_row_input[2]
    result = []
    game_done = False

    # Create a virtual play board
    board = np.zeros((row, column))

    # Playing procedure
    if win <= row or win <= column:
        count = 0                                                   # Variable to check the game's completeness
        last_move_player = 1
        while game_done == False:
            input_col = s_int(f.readline())                         # The player's move
            count += 1
            check_end_game = check_end(count, column, row, result)
            if check_end_game is not None:
                result = check_end_game
                break
            else:
                if input_col > column:                                      # Conditions for the invalid column game
                    result = 6
                    break
                else:
                    last_move_col = input_col - 1   # -1 to be in range 0...(Column-1)
                    last_move_row = check_slot(last_move_col,board)
                    if last_move_row is not None:   # Condition for the valid move, , checking the row's availability
                        board[last_move_row][last_move_col] = last_move_player
                        last_move_player_win = check_win(count, board, last_move_player,
                                                         last_move_col, last_move_row, win)
                        # last_move_player_win will return either 1, 2 or None
                        if last_move_player_win:    # Winning condition
                            if f.readline() != '':  # If players are still playing
                                result = 4
                                break
                            else:
                                result = last_move_player_win
                                break
                        else:
                            if last_move_player == 1:
                                last_move_player = 2
                            else:
                                last_move_player = 1
                    else:
                        result = 5
                        break
        print(result)
    else:
        result = 7
        print(result)
