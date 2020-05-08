#!/usr/bin/env checkio --domain=py run the-longest-palindromic

# Write a function that finds the longestpalindromicsubstring of a given string. Try to be as efficient as possible!
# 
# If you find more than one substring, you should return the one that’s closer to the beginning.
# 
# Input:A text as a string.
# 
# Output:The longest palindromic substring.
# 
# Precondition:1<|text| ≤ 20
# The text contains only ASCII characters.
# 
# 
# END_DESC

def polindr (list0):
    if list0 == list0[-1::-1]:
        return True 
    else:
        return False

def longest_palindromic(a):
    
    for i in range(len(a), 0, -1):
        print('i = ', i)
        for j in range(0, (len(a)-i+1)):
            print('j = ', j)
            if polindr (a[0+j: 0+j+i]):
                return a[0+j: 0+j+i]
   



"""
if __name__ == '__main__':
    print("Example:")
    print(longest_palindromic('abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")"""