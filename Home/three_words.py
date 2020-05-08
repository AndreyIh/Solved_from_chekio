#!/usr/bin/env checkio --domain=py run three-words

# Let's teach the Robots to distinguish words and numbers.
# 
# You are given a string with words and numbers separated by whitespaces (one space).    The words contains only letters.    You should check if the string contains three words insuccession.    For example, the string "start 5one two three7 end" contains three words in succession.
# 
# Input:A string with words.
# 
# Output:The answer as a boolean.
# 
# Precondition:The input contains words and/or numbers. There are no mixed words (letters and digits combined).
# 0 < len(words) < 100
# 
# 
# END_DESC

def checkio(words: str) -> bool:
    words = words.split()
    n = 0
    for i in words:
        if not i.isdigit():
            n +=1
            if n >= 3:
                return True
        else:
            n = 0
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")