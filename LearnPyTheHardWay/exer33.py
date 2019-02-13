#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# ex33: While-Loops

i = 0
numbers = []

while i < 6:
    print("At the top i is {}".format(i))
    numbers.append(i)

    i = i + 1
    print("Numbers Now: ",numbers)
    print("At the bottom i is {}".format(i))

print("The numbers: ")

for i in numbers:
    print(i)




