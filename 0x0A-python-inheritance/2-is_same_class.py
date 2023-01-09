#!/usr/bin/python3
'''
is_same_class function
'''


def is_same_class(obj, a_class):
    '''
    Returns True if obj is exactly an instance of a_class;
    Otherwise, False
    '''
    return (type(obj) == a_class)
