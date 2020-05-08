#!/usr/bin/env checkio --domain=py run ascending-list

# Determine whether the sequence of elements items is  ascending so that its each element is  strictly larger   than (and not merely equal to) the element that precedes it.
# 
# Input:Iterable with ints.
# 
# Output:Bool.
# 
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    items1=items[:]
    items1.sort()
    if len(items) < 2:
        return True
    return items == items1 and items[0] != items[-1]

if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")