#!/usr/bin/env checkio --domain=py run digits-multiplication

# You are given a positive integer.    Your function should calculate the product of the digits excluding any zeroes.
# 
# For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
# 
# Input:A positive integer.
# 
# Output:The product of the digits as an integer.
# 
# Precondition:0 < number < 106
# 
# 
# END_DESC

def checkio(number: int) -> int:
    p = 1
    for i in str(number):
        if i != "0":
            p *= int(i)
    return p


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")