#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_dict = {}
    for key, value in a_dictionary.items():
        multiplied_dict[key] = 2 * value
    return multiplied_dict
