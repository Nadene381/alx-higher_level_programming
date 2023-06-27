#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        index = 0
        for i in my_list:
            print(i, end=' ')
            index += 1
            if index == x:
                break
        print()
        return index
    except TypeError:
        print("Error: Invalid element")
        return index
