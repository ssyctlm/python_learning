def cheese_and_cracker(cheese_count,boxes_of_crackers):
	print('You have {} cheeses!'.format(cheese_count))
	print('You have {} boxes of crackers!'.format(boxes_of_crackers))
	print("Man that's enough for a party!")
	print('Get a blanket.\n')
	
print("We can just give the function number directly:")
cheese_and_cracker(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amonut_of_crackers = 50

cheese_and_cracker(amount_of_cheese,amonut_of_crackers)

print('We can even do math inside too:')
cheese_and_cracker(10+20,5+6)


print("And we can combine the two, variables and math:")
cheese_and_cracker(amount_of_cheese + 100,amonut_of_crackers + 1000)


