#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value) == value:
            print("{:d}".format(value))
            print()
            return True
        else:
            return False
    except (ValueError, TypeError):
        return False
