#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# ex35: Branches and Functions

from sys import exit

def gold_room():
    """This is a treasury room , if you type strings, you will die
        if you take too many money ,you will die
        good luck
    """
    print("This room is full of gold. How much do you take?")

    next = input(">>>")
    if '0' in next or '1' in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def my_gold_room():
    print("This room is full of gold. How much do you take?")

    try:
        next =int(input("Enter a number: >>>"))
    except:
        print("You didn't enter a number as informed")
        dead("Man, learn to type a number")
    else:
        if next < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        else:
            dead("You greedy basterd")


def bear_room():
    """This is a bear_room scene.
        you have 3 options to choice from:
        take money, you will die
        taunt twice ,you will die

    """
    print("There is a bear here.\nThe bear has bunch of honey. \nThe fat bear is in front of another door. \nHow are"
          " you going to move the bear")
    bear_moved = False

    while True:
        next = input(">>>")
        if next == 'take honey':
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear " and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            my_gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu. \nHe, it, whatever stares at you and you go insane."
          "\nDo you flee for your life or eat your head?")

    next = input(">>>")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why,"Good job!")
    exit(0)

def start():
    print("You are in a dark room. \nThere is a door to your right and left. \nWhich one do you take?")

    next = input(">>>")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
