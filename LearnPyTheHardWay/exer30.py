people = 30
cars = 40
buses = 15

if cars > people:
    print("We should be take the cars.")
elif Cars < people:
    print("We shoud not take the cars.")
else:
    print("We can't decide")


if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, Let's stay home then")

if people > cars and buses < cars:
    print(" False",people > cars and buses < cars)
elif people < cars and buses< cars:
    print("True",people < cars and buses< cars)
else:
    print('whatsoever')

