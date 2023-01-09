#!/usr/bin/python3
'''
is_kind_of_class function
'''


def is_kind_of_class(obj, a_class):
    '''
    Returns True if obj is an instance, or an instance of an inherited
    class of a_class; Otherwise False
    '''
    return (isinstance(obj, a_class))
