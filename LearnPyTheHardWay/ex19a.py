def apple(yellow,red):
	print "I have %d yellow apples" % yellow
	print "I have %d red apples" % red
	

	
def multipal (snow,white):
	return snow*white

def add (hello,world):
	return hello+world
	
apple (10,15)

a = 20.0
b = 25.0
apple(a,b)

apple (15*15,16*16)

apple (a/10,b/10)

multipal(3,5)

apple(multipal(3,5),add(3,5))

A=int(raw_input("how many reds do you have"))
B=int(raw_input("how many yellow do you have"))
apple(A,B)

