#!/usr/bin/python3
import sys
number_argum = len(sys.argv) - 1
if number_argum == 0:
    print(f"{number_argum} arguments.")
elif number_argum == 1:
    print(f"{number_argum} argument:")
    print(f"1: {sys.argv[1]}")
else:
    print(f"{number_argum} arguments:")
    n = 1
    while n <= number_argum:
         print(f"{n}: {sys.argv[n]}")
        n += 1
    if __name__ == "__main__":
    pass
