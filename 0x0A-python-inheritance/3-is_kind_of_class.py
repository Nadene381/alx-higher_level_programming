#!/usr/bin/python3
'''
   Function that check if a especific object is a kind of instance of a class
'''


def is_kind_of_class(obj, a_class):
    '''
        Function that check if object belongs a class or heritance
        arguments:
            obj: object
            a_class: class to check
        Return:
            True or false
    '''
    return isinstance(obj, a_class)
