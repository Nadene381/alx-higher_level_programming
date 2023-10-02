#!/usr/bin/python3
'''
    Function that check if a object is from a especific subclass
'''


def inherits_from(obj, a_class):
    '''
       Function that check if object belongs a class or heritance but not a superclass
        arguments:
            obj: object
            a_class: class to check
        Return:
            True or false
    '''
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
