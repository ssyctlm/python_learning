def add(a,b):
	print("Adding {} + {} ".format(a,b))
	return a+b #Return means after the exercution of a function it can gave the result as an argument to a variable which we can use directly
	
def subtract(a,b):
	print('Subtracting {} - {}'.format(a,b))
	return a-b
	
def multiply(a,b):
	print('Multiplying {} * {}'.format(a,b))
	return a*b
	
def divide(a,b):
	print('Dividing {} / {}'.format(a,b))
	return a/b
	

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print("Age: {} \nHeight: {} \nWeight: {} \nIQ: {}".format(age,height,weight,iq))


# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))#Python will exercute a complex function from the most insde to outer, in another word , the content in the deepest parentheses will run first

print("That becomes: ", what, "Can you do it by hand?")

print(subtract(add(24,divide(34,100)),1023))
