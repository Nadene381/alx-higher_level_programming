#!/usr/bin/python3
def print_last_digit(number):
    num_string = str(number)
    last_num = int(num_string[-1])
    print(last_num, end="")
    return last_num
