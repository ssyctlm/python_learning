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



def player_input():
	
	player1 = ''
	judge = False
	
	
	while judge == False:
		player1 = input("What sign do you want to ues? 'O' or 'X'?")
		
		if player1 == 'O' or player1 =='X':
			print("OK! You chose %s" %player1)
			return ('O','X')
			judge = True
		elif player1 == 'o' or player1 == 'x':
			print("You should type Capital letter")
		else:
			print("You must choose a sign first! ")
			
			
def place_marker(board, marker, position):
	#board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	board[(position-1)] = marker
	
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)			
place_marker(test_board,'$',8)
display_board(test_board)

		
'''		Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.'''
		
		
		
		
#player_input()
