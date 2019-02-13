

#1. Players choose a mark
def choose_mark():
    #player1_name = input("Please enter your name: >>>")
    print("hello Player1, welcome to the tic-toc game!")
    while True:
        ch_mk = input("Choose a mark first, \"O\" or \"X\" ?")
        if ch_mk.upper() == "O":
            print("\nOk, you've chosen {}".format(ch_mk.upper()))
            return ("O","X")
            # break 为什么不需要break？
        elif ch_mk.upper() == "X":
            print("\nOk, you've chosen {}".format(ch_mk.upper()))
            return("X","O")

        else:
            print("Maybe you made a mistake")

#2. Decide who will go first
def go_first(mark1,mark2):
    if random.choice([0,1]) == 0:
        print("\nplayer1:{} goes first".format(mark1))
        return  0 #"player1:{}".format(mark1)
    else:
        print("\nplayer2:{} goes first".format(mark2))
        return  1 #"player2:{}".format(mark2)

#3. Display the board
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

#4. player1's turn:
	
	#4.1 makesure the board is not full
def check_full(board):
    return ' ' in board[1:]



	
	#4.2 where to put

def check_valid(position, board):
    return check_full(board) and board[position] == ' '
    # if check_full(board) and [position] == ' ':
    #     return True
    # else:
    #     return False
def mark_put(mark,position,board):
    board[position] = mark

	#4.3 check_win:
def check_win(mark,board):
    return (board[1] == board[2] == board[3] == mark or
            board[4] == board[5] == board[6] == mark or
            board[7] == board[8] == board[9] == mark or
            board[1] == board[4] == board[7] == mark or
            board[2] == board[5] == board[8] == mark or
            board[3] == board[6] == board[9] == mark or
            board[1] == board[5] == board[9] == mark or
            board[7] == board[5] == board[3] == mark)
		#4.3.1 if win game over
		
		#4.3.2 no win player2's Turn
def player_input():
    while True:
        try:
            position = int(input("please choose a position to put mark 1-9:"))
        except:
            print("Only number available")
        else:
           return position


# global
import random
game = True
player1_mark,player2_mark = choose_mark()
board = [' ']*10
print(check_full(board))
turn = go_first(player1_mark,player2_mark)
print(turn)
# print(turn, "will go first")
input("\n=======>>>>\nPress any key to start")
display_board(board)

while game:
#player1:
    if turn == 0:
        print("player1's turn")
        position = player_input()
        if check_valid(position, board):
            mark_put(player1_mark, position, board)

        else:
            print("This position is not valid, put somewhere else!")


        display_board(board)
        if check_win(player1_mark,board):
            print("player1",player1_mark,"Win!")
            game = False
            break
        elif not check_full(board):
            print("The board is full , you are even!")
            game = False
            break
        else:
            turn = 1


#player2:
    elif turn == 1:
        print("player2's turn")
        position = player_input()
        if check_valid(position, board):
            mark_put(player2_mark, position, board)

        else:
            print("This position is not valid, put somewhere else!")
        display_board(board)
        if check_win(player2_mark, board):
            print("player2", player2_mark, "Win!")
            game = False
            break
        elif not check_full(board):
            print("The board is full , you are even!")
            game = False
            break
        else:
            turn = 0




