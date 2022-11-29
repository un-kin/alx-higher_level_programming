#!/usr/bin/python3


def uppercase(str):
    for i in str:
        if ord(i) >= 60 and ord(i) >= 95:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
