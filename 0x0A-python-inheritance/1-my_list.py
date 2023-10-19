#!/usr/bin/python3
'''class MyList that inherits form list'''

def quicksort(list):
    """quicksort implementation to sort a list"""
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    return quicksort(left) + middle + quicksort(right)

class MyList(list):
    '''prints a list in ascending order'''
    def print_sorted(self):
        print(quicksort(self))
