from random import randint

board = []
board2 = []
for x in range(11):
    board.append(["O"] * 11)

for x in range(11):
    board2.append(["V"] * 11)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
    
def random_row1(board):
    return randint(0, len(board) - 1)

def random_col1(board):
    return randint(0, len(board[0]) - 1)

def random_row2(board):
    return randint(0, len(board) - 1)

def random_col2(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
ship_row1 = random_row1(board)
ship_col1 = random_col1(board)
ship_row2 = random_row1(board)
ship_col2 = random_col1(board)

#print ship_row
#print ship_col
#print ship_row1
#print ship_col1
#print ship_row2
#print ship_col2
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(21):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    
    if (guess_row == ship_row) and (guess_col == ship_col):
        print ("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "S"
        print_board(board)
    elif (guess_row < 0) or (guess_col < 0):
        print ("Sorry, Invalid commadand")
        break
    elif (guess_row == ship_row1) and (guess_col == ship_col1):
        print ("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "S"
        print_board(board)
    elif (guess_row == ship_row2) and (guess_col == ship_col2):
        print ("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "S"
        print_board(board)
    elif (board[ship_row][ship_col] == "S") and (board[ship_row1][ship_col1] == "S") and  (board[ship_row2][ship_col2] == "S"):
        print("You Won")
        board2[ship_row][ship_col] = "Sunk"
        board2[ship_row1][ship_col1] = "Sunk"
        board2[ship_row2][ship_col2] = "Sunk"
        print_board(board2)
        break
    else:
        if (guess_row < 0 or guess_row > 10) or (guess_col < 0 or guess_col > 10):
            print("Oops, that's not even in the ocean.")
        elif (board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        
        if turn == 20:
            print ("Game Over. Thanks for playing")
            print (ship_row)
            print (ship_col)
            print (ship_row1)
            print (ship_col1)
        # Print (turn + 1) here!
        print ("Turn", turn + 1)
        print_board(board)
