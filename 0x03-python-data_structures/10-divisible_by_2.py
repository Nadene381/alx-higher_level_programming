#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    results = []
    for n in my_list:
        results.append(n % 2 == 0)
    return results
