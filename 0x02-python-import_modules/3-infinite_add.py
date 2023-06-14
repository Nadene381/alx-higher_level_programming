#!/usr/bin/python3
import sys
total_sum = 0
if __name__ == '__main__':
    for n in sys.argv[1:]:
        total_sum += int(n)
    print(total_sum)
