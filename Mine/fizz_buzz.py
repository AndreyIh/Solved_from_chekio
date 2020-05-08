#!/usr/bin/env checkio --domain=py run fizz-buzz

# "Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.
# 
# You should write a function that will receive a positive integer and return:
# "Fizz Buzz"if the number is divisible by 3 and by 5;
# "Fizz"if the number is divisible by 3;
# "Buzz"if the number is divisible by 5;
# The numberas a string for other cases.
# 
# 
# Input:A number as an integer.
# 
# Output:The answer as a string.
# 
# Precondition:0 < number ≤ 1000
# 
# 
# END_DESC

# Your optional code here
# You can import some modules or create additional functions


def checkio(number: int) -> str:
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check.
    if number % 5 == 0 and number % 3 == 0:
        ret = 'Fizz Buzz'
    elif number % 5 == 0:
        ret = 'Buzz'
    elif number % 3 == 0:
        ret = 'Fizz'
    else:
        ret = str(number)
    
    return ret

# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio(15))
    
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")