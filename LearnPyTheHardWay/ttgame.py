import random
board = ['#','','','','','','','','','']
# 1. here is the board
def display_board(qi):
	#qi = ['','','','','','','','','']
	print('|   |   |   |   ')
	print('|',qi[6],'|',qi[7],'|',qi[8],'|')
	print('|   |   |   |   ')
	print('-------------')
	print('|   |   |   |   ')
	print('|',qi[3],'|',qi[4],'|',qi[5],'|')
	print('|   |   |   |   ')
	print('-------------')
	print('|   |   |   |   ')
	print('|',qi[0],'|',qi[1],'|',qi[3],'|')
	print('|   |   |   |   ')

# 2. choose a mark
def mark_choose():
	print('Player1 what mark do you want to use? O or X?')
	while True:
		player1 = input('>>>')
		if player1.upper() == 'O':
			print('Ok, player1 chose {}'.format(player1.upper()))
			return ('O','X')
			break
		elif player1.upper() == 'X':
			print('Ok, player1 chose {}'.format(player1.upper()))
			return ('X','O')
			break
		else:
			print('You should enter X or O ')
			
# 3.roll for first hand
def who_first():
	player1 , player2 = mark_choose()
	first_hand = random.randint(0,1)
	if first_hand == 0:
		print(f'Player1: {player1} goes first')
		return player1
	else:
		print(f'Player2: {player2} goes first')
		return player2
		
# 4. put a sign on board if avilable
def put_sign(player):
	display_board(board)
	while True:
		try:
			put = int(input('Position 1 to 9: >>>'))
		except :
			print('Number between 1 and 9 ONLY')
		else:
			if board[put] == '':
				board[put] = player
				
			


			
			
def place_marker(board, marker, position):
	#board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	board[(position-1)] = marker
	
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)			
place_marker(test_board,'$',8)
display_board(test_board)

		
'''		Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.'''
		
#print(mark_choose())
for i in range(20):
	print(who_first())
		
		
#player_input()

# 1. have a board
# 2. choose a mark
# 3. roll for first hand
# 4. put a sign on board if avilable
# 5. check win check draw


