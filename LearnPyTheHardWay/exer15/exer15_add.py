filename = input("Which file do you want to open?")

print("Ok,file-%r opened:"% filename)

readtxt = open(filename)

print(readtxt.read())

readtxt.close()
