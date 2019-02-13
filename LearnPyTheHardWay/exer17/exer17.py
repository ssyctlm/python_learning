from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file,to_file))

# We could do these two on one line too, how?
inputt = open(from_file)
indata = inputt.read()

print("The input file is {} bytes long".format(len(indata)))

print("Does the output file exist? {}".format(exists(to_file)))

print("Ready, hit RETURN to continue, CTRL-C to abort")

input(">>>")

output = open(to_file,"w")
output.write(indata)

print("Alright, all done.")



output.close()
inputt.close()


