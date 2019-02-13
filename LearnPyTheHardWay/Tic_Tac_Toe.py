### Step1: 3*3 board display


import random


def display_board(board):
    lst = [n for n in range(11)]
    print("   |", "   |", "   ",'\t',"   |", "   |", "   ")
    print("", lst[7], "|", "", lst[8], "|", "", lst[9]," ",'\t',"", board[7], "|", "", board[8], "|", "", board[9])
    print("   |", "   |", "   ",'\t',"   |", "   |", "   ")
    print('-------------','\t','-------------')
    print("   |", "   |", "   ",'\t',"   |", "   |", "   ")
    print("", lst[4], "|", "", lst[5], "|", "", lst[6]," ",'\t',"", board[4], "|", "", board[5], "|", "", board[6])
    print("   |", "   |", "   ",'\t',"   |", "   |", "   ")
    print('-------------','\t','-------------')
    print("   |", "   |", "   ",'\t',"   |", "   |", "   ")
    print("", lst[1], "|", "", lst[2], "|", "", lst[3]," ",'\t',"", board[1], "|", "", board[2], "|", "", board[3])
    print("   |", "   |", "   ",'\t',"   |", "   |", "   ")


# call board to test if it worKS
#qi = ["0","1","2","3","4","5","6","7","8","9"]
#display_board(qi)


### Step2: Player choose their marker"X" or "O"


def player_input():
    player1 = ' '
    while True:
        playeer_mark = input("Please choose a marker, 'O' or 'X' ?").lower()
        if playeer_mark != 'x' or playeer_mark != 'o':
            if playeer_mark == 'x':
                print("OK, you chose '%s'" % playeer_mark.upper())
                return('X', 'O')
            elif playeer_mark == 'o':
                print("OK, you chose '%s'" % playeer_mark.upper())
                return('O', 'X')
            else:
                print("You should choose from 'X' and 'O'")


# call board to test if it worKS
#player_input()


### Step3 Write a function that takes in the board list object, a marker ('X' or 'O'),
###       and a desired position (number 1-9) and assigns it to the board.


def place_marker(board, marker, position):
    board[position] = marker


# test_board = ['#','X','O','X','O','X','O','X','O','X']
# place_marker(test_board,'$',8)
# display_board(test_board)


### Step4 Write a function that takes in a board and a mark (X or O)
##        and then checks to see if that mark has won. *


def win_check(board, mark):
    return (board[1] == board[2] == board[3] == mark or
            board[4] == board[5] == board[6] == mark or
            board[7] == board[8] == board[9] == mark or
            board[1] == board[4] == board[7] == mark or
            board[2] == board[5] == board[8] == mark or
            board[3] == board[6] == board[9] == mark or
            board[1] == board[5] == board[9] == mark or
            board[7] == board[5] == board[3] == mark)


# win_check(test_board,'X')


### Step5 Write a function that uses the random module to randomly decide which player goes first.
### You may want to lookup random.randint() Return a string of which player went first.


def choose_first(player1,player2):
    ran_player =  random.randint(1,2)
    if ran_player == 1:
        print("player1 goes first!")
        return player1
    else:
        print("Player2 goes first! ")
        return player2


### Step 6: Write a function that returns a boolean indicating
###         whether a space on the board is freely available.


def space_check(board, position):
    return board[position] == ' '


### Step 7: Write a function that checks if the board is full
###         and returns a boolean value. True if full, False otherwise.


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


### Step 8: Write a function that asks for a player's next position (as a number 1-9)
###         and then uses the function from step 6 to check if it's a free position.
###         If it is, then return the position for later use.


def player_choice(board):
    while True:
        enter = input("Where do you want to put your mark? 1-9")
        if enter in ['1','2','3','4','5','6','7','8','9']:
        	position = int(enter)
        	if space_check(board,position):
        		return position
        	elif not space_check(board,position):
        		print("This position is occupied, you should choose another position(1-9)")


### setp9  Write a function that asks the player if they want to play again and
###        returns a boolean True if they do want to play again.


def replay():
    while True:
        re_play = input("Do you want to play again? 'Yes' or 'No'?").lower()
        if re_play.startswith('y'):
            return True
        elif re_play.startswith('n'):
            return  False
        else:
            print("You made a typro,please confirm again")


### Game


print('Welcome to Tic Tac Toe!')

while True:
    print('\n' * 100)
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first(player1_marker,player2_marker)
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

