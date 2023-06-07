#!/usr/bin/python3
print(", ".join("{:d}{:d}".format(n, d) for n in range(10)
                for d in range(n + 1, 10)),
      end="")
print("\n", end="")
