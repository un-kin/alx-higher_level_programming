#!/usr/bin/python3
res = ""
for alaphabet in range(97, 123):
    if alaphabet != 101 and alaphabet != 113:
        res = chr(alaphabet)
        print("{}".format(res), end="")
