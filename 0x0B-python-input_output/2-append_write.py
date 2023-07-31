#!/usr/bin/python3
"""A function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """ Function that append to a file"""

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
