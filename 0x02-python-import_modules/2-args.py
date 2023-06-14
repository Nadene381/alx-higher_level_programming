#!/usr/bin/python3
import sys
number_argum = len(sys.argv) - 1
if number_argum == 0:
    print(F"{number_argum} arguments.")
elif number_argum == 1:
    print(F"{number_argum} argument:")
    print(f"1: {sys.argv[1]}")
else:
    print(F"{number_argum} arguments:")
    n = 1
    while n <= number_argum:
        print("{}: {}".format(n, sys.argv[n]))
        n += 1
    if __name__ == "__main__":
    pass
