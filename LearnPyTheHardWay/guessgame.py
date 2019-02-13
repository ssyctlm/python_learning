import random

def guess_number(say):
	'''A Guess Number Game'''
	print('Hello',say)
	print('You have 6 tries to guess a number between 1 to 99')
	guess = 0
	answer = random.randint(1,100)
	while guess < 6:
		try:
			try_guess = int(input('What\'s your guess? >>>'))
		except :
			print('Only number please!')
		else:
			if try_guess > 100 or try_guess < 1:
				print('Your guess is out of range')
			elif try_guess > answer:
				guess += 1
				print("Your guess is bigger, please try again. \nYou have {} time left.".format(6-guess))
			elif try_guess < answer:
				guess += 1
				print("Your guess is smaller, please try again. \nYou have {} time left.".format(6-guess))
			else:
				print("Great! You get it")
				break
	print('The answer is {}'.format(answer))
	
				
		
		
guess_number('macky')
	
