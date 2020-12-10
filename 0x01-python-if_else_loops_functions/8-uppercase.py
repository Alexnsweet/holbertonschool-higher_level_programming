#!/usr/bin/python3
def uppercase(str):
    for i in str:
        letter = ord(i)
        if letter in range(97, 123):
            letter = letter - 32
        print("{:c}".format(letter), end='')
    print("")
