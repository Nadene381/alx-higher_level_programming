#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
answer_of_add = add(a, b)
answer_of_sub = sub(a, b)
answer_of_mul = mul(a, b)
answer_of_div = div(a, b)
print("{} + {} = {}".format(a, b, answer_of_add))
print("{} - {} = {}".format(a, b, answer_of_sub))
print("{} * {} = {}".format(a, b, answer_of_mul))
print("{} / {} = {}".format(a, b, answer_of_div))
if __name__ == "__main__":
    pass
