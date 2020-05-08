#!/usr/bin/env checkio --domain=py run isometric-strings

# Maybe it's a cipher? Maybe, but we don’t know for sure.
# 
# Maybe you can call it"homomorphism"? i wish I know this word before.
# 
# You need to check that the 2 given strings are isometric. This means that a character from one string can become a match for characters from another string.
# 
# One character from one string can correspond only to one character from another string. Two or more characters of one string can correspond to one character of another string, but not vice versa.
# 
# 
# END_DESC

def isometric_strings(str1: str, str2: str) -> bool:
    a = len(set(list(i for i in str2))) <= len(set(list(i for i in str1)))
    a1, a2 =[0],[0]
    for i in range(1,len(str1)):
        
        if str1[i]==str1[i-1]:
            a1.append(a1[i-1])
        else:
            a1.append(a1[i-1]+1)
            
        if str2[i]==str2[i-1]:
            a2.append(a2[i-1])
        else:
            a2.append(a2[i-1]+1)
    print(a1,a2)
    b = (a1 == a2)
    if a == True:
        return True if b else False
    return False


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))
    print(isometric_strings("hall","hoop"))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")