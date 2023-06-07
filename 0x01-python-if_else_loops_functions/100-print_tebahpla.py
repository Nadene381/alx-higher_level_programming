#!/usr/bin/python3
print(''.join("{:c}".format(n) if n % 2 == 1
              else "{:c}".format(n + 32) for n in range(90, 64, -1)), end='')
