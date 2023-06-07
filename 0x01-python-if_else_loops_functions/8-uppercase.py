#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if 'a' <= n <= 'z':
            uppercase_char = chr(ord(n) & ~32)
        else:
            uppercase_char = n
        print("{}".format(uppercase_char), end='')
    print()
