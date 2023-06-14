#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_that_sorted = sorted(a_dictionary.keys())
    for n in keys_that_sorted :
        print(n, ":", a_dictionary[n])
