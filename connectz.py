import sys


def check_slot(column_selection, board, row):
    # Check whether the move exceeds the limit
    if len(board[column_selection]) > row:
        print('5')
        sys.exit()


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
    # Checking file location
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


def check_win_h(count, board, last_move_player, last_move_col, last_move_row, win, column):
    # Check win horizontally
    if count + 1 >= 2 * win:
        check_target = 1
        for i in [1, -1]:
            cw_col = last_move_col
            cw_row = last_move_row
            while (0 <= cw_col + i < column
                   and 0 <= cw_row < len(board[cw_col+i]) and board[cw_col + i][cw_row] == last_move_player):
                check_target += 1
                cw_col += i
                if check_target == win:
                    return last_move_player


def check_win_v(count, board, last_move_player, last_move_col, last_move_row, win):
    # Check win vertically
    if count + 1 >= 2 * win and last_move_row >= win - 1:
        check_target = 1
        cw_row = last_move_row
        cw_col = last_move_col
        while 0 <= cw_row - 1 and board[cw_col][cw_row - 1] == last_move_player:
            check_target += 1
            cw_row += -1
            if check_target == win:
                return last_move_player


def check_win_nwse(count, board, last_move_player, last_move_col, last_move_row, win, column):
    # Check win North West to South East
    if count + 1 >= 2 * win:
        check_target = 1
        for i in [1, -1]:
            cw_row = last_move_row
            cw_col = last_move_col
            while (0 <= cw_col + i < column
                   and 0 <= cw_row - i < len(board[cw_col+i]) and board[cw_col + i][cw_row - i] == last_move_player):
                check_target += 1
                cw_row += -i
                cw_col += i
                if check_target == win:
                    return last_move_player


def check_win_swne(count, board, last_move_player, last_move_col, last_move_row, win, column):
    # Check win South West to North East
    if count + 1 >= 2 * win:
        check_target = 1
        for i in [1, -1]:
            cw_row = last_move_row
            cw_col = last_move_col
            while (0 <= cw_col + i < column
                   and 0 <= cw_row + i < len(board[cw_col+i]) and board[cw_col + i][cw_row + i] == last_move_player):
                check_target += 1
                cw_row += i
                cw_col += i
                if check_target == win:
                    return last_move_player


def check_win(count, board, last_move_player, last_move_col, last_move_row, win, column):
    # Combine all directional check_win_ functions above
    win_h = check_win_h(count, board, last_move_player, last_move_col, last_move_row, win, column)
    if win_h:
        return win_h
    win_v = check_win_v(count, board, last_move_player, last_move_col, last_move_row, win)
    if win_v:
        return win_v
    win_nwse = check_win_nwse(count, board, last_move_player, last_move_col, last_move_row, win, column)
    if win_nwse:
        return win_nwse
    win_swne = check_win_swne(count, board, last_move_player, last_move_col, last_move_row, win, column)
    if win_swne:
        return win_swne
    return 0


def check_end(count, column, row):
    if input_col == -1 and count - 1 < column * row:  # Conditions for the incomplete game
        print('3')
        sys.exit()
    elif input_col == -1 and count - 1 == column * row:  # Conditions for the draw game
        print('0')
        sys.exit()


def check_game_eligi(win, row, column):
    # Check the game's form
    if win > row or win > column:
        print('7')
        sys.exit()


def check_input(col, column):
    # Check the input's eligibility
    if col > column:  # Condition for the invalid column game
        print('6')
        sys.exit()


def swap_last_move_player(last_move_player):
    # Swap the player
    if last_move_player == 1:
        return 2
    else:
        return 1


if __name__ == '__main__':

    if len(sys.argv) == 1:
        data_file_path = input('Provide one input file: ')
    else:
        data_file_path = sys.argv[1]

    # Read file
    f = read_file(data_file_path)
    first_row_input = parse_first_row_input(f)

    # Define initial variables
    column = first_row_input[0]
    row = first_row_input[1]
    win = first_row_input[2]
    last_move_player = 1
    last_move_player_win = 0
    count = 0       # Variable to check the game's completeness
    board = {}      # Pre-define the play board dictionary

    # Pre-define the "skeleton" for the play board dictionary
    for i in range(column):
        board[i] = []

    # Playing procedure
    check_game_eligi(win, row, column)  # Check whether the game's form is valid

    while last_move_player_win == 0:    # The game is running until we found the player won or the error

        input_col = s_int(f.readline())  # Read each player's move
        count += 1

        check_end(count, column, row)      # Check whether the game is draw or incomplete
        check_input(input_col, column)     # Check input's eligibility

        last_move_col = input_col - 1      # -1 to be in range 0...(Column-1)
        last_move_row = len(board[last_move_col])

        board[last_move_col].append(last_move_player) # Add the player's number to the dictionary
        check_slot(last_move_col, board, row)         # Check whether the newly added number is valid

        last_move_player_win = check_win(count, board, last_move_player,
                                         last_move_col, last_move_row, win, column)
        # last_move_player_win will return either 1, 2 or 0

        if last_move_player_win:  # If one player has won
            if f.readline() != '':  # If players are still playing
                print('4')
                break
            else:
                print('%s' % last_move_player_win)
                break
        else:
            last_move_player = swap_last_move_player(last_move_player)