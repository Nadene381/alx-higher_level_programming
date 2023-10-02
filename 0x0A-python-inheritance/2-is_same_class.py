#!/usr/bin/python3
'''
    Function that check if a especific object is exactly a instance of a class
'''


def is_same_class(obj, a_class):
    '''
        Function that checks if object belongs a class
        arguments:
            obj: object
            a_class: class to check
        Return:
            True or false
    '''
    if type(obj) is a_class:
        return True
    else:
        return False
