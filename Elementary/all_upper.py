#!/usr/bin/env checkio --domain=py run all-upper

# Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.
# 
# Input:A string.
# 
# Output:a boolean.
# 
# Precondition:a-z, A-Z, 1-9 and spaces
# 
# 
# END_DESC

import re
def is_all_upper(text: str) -> bool:
    return re.search(r'[a-z]', text) == None