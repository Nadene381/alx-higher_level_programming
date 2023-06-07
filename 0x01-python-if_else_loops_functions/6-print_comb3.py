#!/usr/bin/python3
for n in range(10):
    for d in range(n + 1, 10):
        print("{:d}".format(n), end="")
        print("{:d}".format(d), end="")
        if n != 8 or d != 9:
            print(", ", end="")
