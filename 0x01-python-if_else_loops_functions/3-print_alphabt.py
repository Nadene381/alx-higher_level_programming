#!/usr/bin/python3
for n in range(ord('a'), ord('z') + 1):
    if chr(n) not in ['q', 'e']:
        print("{}".format(chr(n)), end='')
