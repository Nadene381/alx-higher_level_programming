#!/usr/bin/python3
'''
    A Class that inherits from list
'''


class MyList(list):
    '''
        This prints a list
    '''
    def print_sorted(self):
        print(sorted(self))
