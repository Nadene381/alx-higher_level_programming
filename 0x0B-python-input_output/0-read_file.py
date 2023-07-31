#!/usr/bin/python3
""" A funtion that reads a text file """


def read_file(filename=""):
    """ Function that reads from a file
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        readfile = f.read()
        print(readfile, end='')
