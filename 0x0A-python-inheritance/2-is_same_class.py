#!/usr/bin/python3
"""contains function to check class instance"""

def is_same_class(obj, a_class):
    """ returns true of obj is an instance of a_class,
        False otherwise
     """
    return type( obj ) == a_class
