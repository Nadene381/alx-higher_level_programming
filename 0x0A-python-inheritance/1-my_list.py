#!/usr/bin/python3
'''
    A Class that inherits from list
'''


class MyList(list):
    '''This prints a list'''
    def print_sorted(self):
        """Function that Prints the list but sorted"""
        print(sorted(self))
