#!/usr/bin/python3
'''
    True if the object is an instance of, or if the 
    object is an instance of a class that inherited 
    from, the specified class ; otherwise False.
'''


def is_kind_of_class(obj, a_class):
    '''
        check if object belongs a class or heritance
        args:
            obj: object
            a_class: class to check
        Return:
            True or false
    '''
    return isinstance(obj, a_class)
