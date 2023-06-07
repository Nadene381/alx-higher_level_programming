#!/usr/bin/python3
for n in range(10):
    for d in range(n + 1, 10):
        print("{:d}{:d}, ".format(n, d), end="")
print()
