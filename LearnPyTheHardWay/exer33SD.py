#!/usr/bin/env python3
# -*-coding:utf-8 -*-

def append_list(mi,mx,step):
    """This function is for adding a range of numbers in a list"""
    list_initialization = []
    i = min(mi,mx)
    print(i)
    it = max(mi,mx)
    print(it)
    while i < it+1:
        list_initialization.append(i)
        i += step

    return list_initialization

def app_list_for(mi,mx,step):
    """This function is for adding a range of numbers to a list by for loop

    """
    list_initialization = []

    if mi > mx:
        n = mx
        m = mi
        print(n, m)

    else:
        n = mi
        m = mx
        print(n, m)


    for i in range(n, m, step):
        list_initialization.append(i)


    return list_initialization

print(append_list(99,233,3))

print(app_list_for(233,99,3))

print(app_list_for(99,233,3))

