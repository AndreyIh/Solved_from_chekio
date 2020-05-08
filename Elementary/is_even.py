#!/usr/bin/env checkio --domain=py run is-even

# Check is the given number is even or not. Your function shoudl return True if the number is even, andFalse if the number is odd.
# 
# Input:Int.
# 
# Output:Bool.
# 
# Precondition:both given ints should be between -1000 and 1000
# 
# 
# END_DESC

def is_even(num: int) -> bool:
    # your code here
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")