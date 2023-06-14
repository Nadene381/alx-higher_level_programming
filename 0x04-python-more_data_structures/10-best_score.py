#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    largest_int = None
    largest_int = float('-inf')
    for key, value in a_dictionary.items():
        if value > largest_int:
            largest_key = key
            largest_int = value
    return largest_key
