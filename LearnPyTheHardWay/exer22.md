## ex1:第一个程序
* print()
* # -*- coding:utf-8 -*-
* 

## ex2:注释和#号
* #

## ex3:数字和数学计算
* 运算符号(着重 / 和 % )

## ex4:变量和命名
* 变量(variable)
使用 = 来变量命名，并给它赋值

## ex5:更多的变量和打印
* 格式化字符串 (format string)
* "%s,%r,%d,%i,%f" % (arg1,arg2,arg3,arg4)
> %r 不管什么都打印出来，调试时用(ex6常见问题)
* f"abcdefg{var}"
* "abcdef {} {}".format(*arg)
问题回答
* 浮点四舍五入
> round()函数，如round(pi,2)

## ex6:字符串和文本
* a字符串 与 b字符串 (**拼接(concatenate)**)连接起来，用+号，如 print(a + b)。 字符串和数字或者变量拼接，用,号，如:print(a,1,b)

## ex7:更多打印
* 变量和打印，变量拼接
* python2: print "abcde",
  python3: print("abcde",end="")
  
## ex8:打印，打印

## ex9:打印，打印，打印
* 初次接触转义序列 \n \t \

## ex10:那是什么
*转义序列(escape sequences)
如果出现多个'或者"时，用\来让它正常显示

## ex11:提问
* input()
input 取出的值都是字符串，取整数时需要int(input('abcdef))

## ex12:提示别人
* a = input('hint')
* pydoc input

## ex13:参数(argument)、解包和变量
* from sys import argv
argv(argument variable).这个变量保存着你运行python脚本时传递给python脚本的参数。

## ex14:提示和传递
* input 和 argv 组合使用

## ex15:读取文件
* txt = open(filename)
filename 应该是字符串类型
* txt.read()
read()是一个方法或者函数

## ex16:读写文件
* txt = open(filename,'w')-write
* txt = open(filename,'r')-read
* txt = open(filename,'a')-append
* txt = open(filename,'w+') r and w at the same time
* txt = open(filename,'r+')
* .close()
* .read()
* .readline()
* .readlines()
* .truncate()
* .write(stuff)
* .seek()

## ex17:更多文件操作
* 课后题3

## ex18:命名、变量、代码、和函数
* def
define 
* func_name
the name of the function
* (arg)
*args(asterisk args)
* :

* 4 space

* func_name(args) -call it

## ex19:函数和变量
展示了函数的各种参数传递方式，函数会将传入的内容打印出来。我们可以直接给函数传递数字，也可以给它变量，还可以给它数学表达式，甚至可以把数学表达式和变量合起来用。
从一方面来说，函数的参数和生成变量时用的=赋值符类似。事实上，**如果一个物件可以用=对其命名，通常也可以将其作为参数传递给一个函数。**

可以调用函数并把它当成变量传递给另一个函数

## ex20:函数和文件
* f.seek(0)
每次运行它，就像磁带一样，又回到了最开始(0字节处)
* f.readline()
会读取文件每一行，然后讲"磁头"移动到\n后
* +=

## ex21:函数可以返回某些东西
* return
之前使用=给变量命名，以及将变量定义为某个数字或者字符串。接下来演示的是如何使用=以及一个新的Python词汇return来将变量设置为“一个函数的值”。
python进行计算，然后当函数结束的时候，它就可以以运算结果赋予一个变量

## ex24:更多联系

## ex25:更多更多的练习
* stuff.split('')
Split a sentence into several words and created a list at the same time to contain them
* sorted(list)
* list.pop(0)
0: the fist element; -1:the last element
* import exer25 // from exer25 import *
don't need the ".py" suffix when you import an module  
* module.func()
If you didn't import a specifical function, you need to call it by above command
* help(exer25) and help(ex25.break_words)
The ''' symbol is called "Documentation comments(文档备注）" which will introduce you what this module for and what the fucntion of methods. 
* 把你脚本里的内容逐行通过python编译器执行，看看回事什么样子。你可以执行Ctrl-D（windows里Ctrl-z)来关闭编译器。

## ex28:布尔（boolean）表达式练习
1. 找到相等判断的部分（== or !=),将其改为最终值（True或False)
2. 找到括号里的and/or,先算出它们的值。
3. 找到每一个not，算出他们的相反值。
4. 找到剩下的and/or，解出它们的值。
5. 等你都做完后，剩下的结果就是True 或者 False了


## ex35:分支和函数 Branches and Functions
*  normal boolean logic (with 0==False)
*  Python程序有两种退出方式： os._exit() 和 sys.exit()。我查了一下这两种方式的区别。
  * os._exit() 会直接将python程序终止，之后的所有代码都不会执行。
  * sys.exit() 会抛出一个异常: SystemExit，如果这个异常没有被捕获，那么python解释器将会退出。如果有捕获该异常的代码，那么这些代码还是会执行。


