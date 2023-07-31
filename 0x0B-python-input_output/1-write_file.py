#!/usr/bin/python3
"""A function that writes a string to a text file """


def write_file(filename="", text=""):def write_file(filename="", text=""):
    """ Function that writes to a text file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
