#!/usr/bin/python3
def pow(a, b):
    result_value = 1
    for _ in range(b):
        result_value *= a
    return a ** b
