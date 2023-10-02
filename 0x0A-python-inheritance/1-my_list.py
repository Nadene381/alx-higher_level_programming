#!/usr/bin/python3
'''
   A Class that iheritance from list
'''


class MyList(list):
    '''
        Funtion that print a list sorted
    '''
    def print_sorted(self):
        print(sorted(self))
