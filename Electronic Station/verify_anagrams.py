#!/usr/bin/env checkio --domain=py run verify-anagrams

# An anagram is a type of word play,    the result of rearranging the letters of a word or phrase to produce a new word or phrase,    using all the original letters exactly once.    Two words are anagrams to each other if we can get one from another by rearranging the letters.    Anagrams are case-insensitive and don't take account whitespaces.    For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.
# 
# You are given two words or phrase. Try to verify are they anagrams or not.
# 
# Input:Two arguments as strings.
# 
# Output:Are they anagrams or not as boolean (True or False)
# 
# Precondition:0<|first_word|<100;
# 0<|second_word|<100;
# Words contain only ASCII latin letters and whitespaces.
# 
# 
# END_DESC

def dictin (dict1):
    dict1 = dict1.lower()
    dict2 = {}
    for i in dict1:
        if i.isalpha():
            if i not in dict2:
                dict2[i] = 1
            else:
                dict2[i] += 1
    return dict2


def verify_anagrams(first_word, second_word):
    d1 = dictin(first_word)
    d2 = dictin(second_word)
    if d1 == d2:
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
    print('ok')