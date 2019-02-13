# ex38: Doing Things To Lists 对列表进行操作

#添加列表元素
# append()
mylist1 = []
mylist1.append(1)
mylist1.append(2)
mylist1.append(3)
mylist1.append(4)
mylist1.append(5)

mylist2 = mylist1[:] #复制列表


mylist1.append(mylist2)

print(mylist1)
print(mylist1[5])#访问列表index对应的值

#interesting thing:
mylist3 = mylist2[:]
mylist3.append(mylist3)
print("trikcy thing:", mylist3)
print("trikcy thing1:", mylist3[5])
print("trikcy thing2:", mylist3[5][5])


# 删除列表元素
# del
print("")
print(mylist1)
print("del value at index 5:")
del mylist1[5]
print(mylist1)

#remove()
print("")
print(mylist1)
mylist1.remove(5)
print("after removing 5 :",mylist1)

# pop()
print("")
print(mylist1)
popout = mylist1.pop() # popout the last digit elements
print("pop 4 from mylist1, and attribute it to popout")
print("Now mylist1:",mylist1,"popout:",popout)
pop1st = mylist1.pop(0)
print(mylist1,"and",pop1st)

# 列表脚本操作符 // 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
# len()
print(len(mylist1))

# + 组合
print("")
a = [1,2,3] + [4,5,6]
print(a)

# * 重复
print("")
b = ["hello!"]* 10
print(b)

# 元素是否存在
print(3 in [1,2,3])

# 迭代
for i in [1,2,3]:
    print(i)

#列表函数
#返回列表最大、最小值
max(mylist1)
min(mylist1)
#将元组转换成列表
list((1,2,3))
#将元素组合成字符串
print(''.join(["h","e",'l','l','o']))



# 列表方法
# list.append()
# list.count(obj) # 统计某个元素在列表里的次数
# list.extend(seq) # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj) # 从列表中找出某个值第一个匹配项的索引位置
# list.insert(index.obj) # 将对象插入列表的索引位置
# list.pop([index=-1]) # 移除列表中的一个元素（默认最后一个元素），并且**返回**该元素的值
# list.remove(obj) # 移除列表中某个值的第一个匹配项
# list.remove() # 反向列表中元素
# list.sort(cmp=None, key=None, reverse=False) # 对原列表进行排序

print("-"*50)

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there's not 10  things in that list, let's fix that")

stuff = ten_things.split(" ")
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) is not 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's {} items now.".format(len(stuff)))

print("There are go: ", stuff)
print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print("#".join(stuff[3:5]))









