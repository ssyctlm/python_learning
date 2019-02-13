from sys import argv

script, from_file, to_file = argv

a = to_file.write(str(open(from_file).read()))

