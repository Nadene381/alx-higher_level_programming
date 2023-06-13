#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    first_value = sentence[0] if l > 0 else None
    return l, first_value
