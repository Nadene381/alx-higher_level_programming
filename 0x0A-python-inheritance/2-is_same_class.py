#!/usr/bin/python3
'''
   Function that checks if an object is exactly an instance of the specified class it will return True otherwise it will return False
'''


def is_same_class(obj, a_class):
    '''
        check if object belongs a class
        args:
            obj: object
            a_class: class to check
        Return:
            True or false
    '''
    if type(obj) is a_class:
        return True
    else:
        return False
