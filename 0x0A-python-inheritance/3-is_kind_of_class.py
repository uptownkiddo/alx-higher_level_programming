#!/usr/bin/python3
"""contains the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """returns True if object is an instance of, or is inherited from,
 the specified class"""
    return isinstance(obj, a_class)
