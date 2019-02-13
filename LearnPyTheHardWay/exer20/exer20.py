from sys import argv

script,input_file = argv

def print_all(f):
	print(f.read()) # Print out whole contents of the target files by read it
	
def rewind(f):
	f.seek(0) # Makes the indicator go back to the begining of the file
	
def print_a_line(line_count,f): # Define a function names 'print_a_line' and 2 variables 'line_count' and 'f' needed to be passed in.
	print(line_count,f.readline())# Print out 'line_count' and add accordant line contents of a file 
	
current_file = open(input_file) # Creat a new variable names 'current_file' and exercute the build-in function to open the file names "input_file"

print("First let's print the whole file: \n")

print_all(current_file) # Call the function 'print_all' with the variable 'current_file'

print("Now let's rewind, kind of like a tape.")

rewind(current_file) # Call the function 'rewind' with the variable 'current_file'

print("Let's print three lines:")

current_line = 1 # Creat a new variable and name it 'current_line' and give it a value 1
print_a_line(current_line,current_file)

current_line += 1 # Variable 'current_line' self-add 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)


