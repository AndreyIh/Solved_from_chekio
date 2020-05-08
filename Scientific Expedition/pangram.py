#!/usr/bin/env checkio --domain=py run pangram

# A pangram (Greek:παν γράμμα, pan gramma, "every letter") or holoalphabetic sentence for a given alphabet is a    sentence using every letter of the alphabet at least once. Perhaps you are familiar with the well known pangram "The    quick brown fox jumps over the lazy dog".
# 
# For this mission, we will use the latin alphabet (A-Z). You are given a text with latin letters and punctuation    symbols. You need to check if the sentence is a pangram or not. Case does not matter.
# 
# Input:A text as a string.
# 
# Output:Whether the sentence is a pangram or not as a boolean.
# 
# Precondition:
# 
# all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
# 0 < len(text)
# END_DESC

def check_pangram(text):
    text = text.lower()
    dict1 = {}
    for i in text:
        if i.isalpha():
            dict1[i] = 1
    return True if len(dict1) == 26 else False
    

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')