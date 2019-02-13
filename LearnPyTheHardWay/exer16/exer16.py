from sys import argv
#sys是python自带模块.
#利用 import 语句输入sys 模块。
#sys.argv 实现从程序外部向程序传递参数
#sys.argv 变量是一个包含了命令行参数的字符串列表, 利用命令行向程序传递参数. 其中,脚本的名称总是 sys.argv 列表的第一个参数
script, filename = argv

print("We're going to erase %r. "% filename)
print("If you don't want that, hit CTRL-C(^c).")
print("If you do want that, hit RETURN.")

input(">>>")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm goint to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write((line3))
target.write("\n")

print("Another method to write the whole sentence")
target.write("%s \n%s \n%s \n" % (line1,line2,line3))

print("And finally, we close it.")
target.close()

print("Ok, next we are going to read it ")
txt = open(filename,'r')
print(txt.read())

txt.close()



