#!/usr/bin/python3
def multiple_returns(sentence):
    lenghts = len(sentence)
    first_value = sentence[0] if lenghts > 0 else None
    return lenghts, first_value
