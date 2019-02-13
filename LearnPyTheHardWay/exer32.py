#!/usr/bin/env python3
# ex32: Loops and lists
# For loops

hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weights = [1,2,3,4]



the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']
#  this first kind of for loop goes through a list

for number in the_count:
	print('This is count {}'.format(number))
	
# same as above
for fruit in fruits:
	print(f'A fruit of type: {fruits}')
	
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print("I got {}".format(i))
	print("I got %r" % i)
	
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
	print("Adding {} to the list.".format(i))
	elements.append(i)
	
# now we can print them out too
for i in elements:
	print('Element was: {}'.format(i))
	
#Study Drills
#2
drill = [n for n in range(0,6)]
for i in drill:
	print('Drills was: {}'.format(i))
	
#Common Student Questions
a = [[1,2,3],[4,5,[6,7]]]
for n in a:
	print(n) 
	for m in n:
		print(m)
		
print('a[1][2][1] = {}'.format(a[1][2][1]))
