#!/usr/bin/python3
for n in range(10):
    for d in range(n + 1, 10):
        print("{:02d}, ".format(n), end="")
        print("{:02d}, ".format(d), end="")
print()
