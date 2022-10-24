def print_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print ('-------------')