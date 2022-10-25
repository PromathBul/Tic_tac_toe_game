from Methods import print_board
from Methods import move_player as move
from Methods import control_win as control

board = range(1,10)
board = list(map(str, board))

count = 0
win = False

while not win:
    print_board(board)
    if count % 2 == 0:
        move('X', board)
    else:
        sign = 'O'
        move(sign, board)
    count += 1
    if count > 4:
        value = control(board)
        if value:
            print(value + ' выиграл.')
            win = True
    if count == 9 and win == False:
        print('Ничья.')
        break
print_board(board)