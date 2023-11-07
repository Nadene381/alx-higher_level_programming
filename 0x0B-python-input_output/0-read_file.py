#!/usr/bin/python3
def read_file(filename=""):
    """
    Function that reads a text file and print its contents to stdout.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        pass  # File doesn't exist, do nothing
