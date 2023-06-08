#!/usr/bin/python3
a = 10
b = 5
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
answer_of_sub = sub(a, b)
answer_of_mul = mul(a, b)
answer_of_add = add(a, b)
answer_of_div = div(a, b)
print(f"{a} + {b} = {answer_of_add}")
print(f"{a} - {b} = {answer_of_sub}")
print(f"{a} * {b} = {answer_of_mul}")
print(f"{a} / {b} = {answer_of_div}")
