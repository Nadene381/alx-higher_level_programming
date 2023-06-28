#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        index = 0
        for i in my_list[:x]:
            print("{}".format(i), end=' ')
            index += 1
        print("")
        return index
    except Error:
        print("Invalid element")
