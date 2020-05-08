#!/usr/bin/env checkio --domain=py run all-upper-ii

# Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False.
# 
# Input:A string.
# 
# Output:a boolean.
# 
# Precondition:a-z, A-Z, 1-9 and spaces
# 
# 
# END_DESC

def is_all_upper(text: str) -> bool:
    return text == text.upper() if (text.split() and text[0].isalpha()) else False