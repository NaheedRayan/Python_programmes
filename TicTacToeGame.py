print("--------😉Welcome to the Tic Tac Toe game 😉--------")

print("\n\nPostions for The board :\n")
print(" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 \n\n")




def printBoard(board):
    print( " " +board[1] + " | " + board[2] + " | " + board[3] )
    print("---+---+---")
    print( " " +board[4] + " | " + board[5] + " | " + board[6] )
    print("---+---+---")
    print( " " +board[7] + " | " + board[8] + " | " + board[9] )

board = {
          1 : ' ', 2 : ' ', 3 : ' ',
          4 : ' ', 5 : ' ', 6 : ' ',
          7 : ' ', 8 : ' ', 9 : ' ' 
        }
turn = 'X'

for i in range(9) :
    printBoard(board)
    
    if i%2 == 0 :
        print("Player 1 turn.\nPlease select a position")
    else :
        print("Player 2 turn.\nPlease select a position")
    x = input()
    move = int(x)
    board[move] = turn 
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
printBoard(board)
print("------Game Over------")
