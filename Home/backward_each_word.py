#!/usr/bin/env checkio --domain=py run backward-each-word

# In a given string you should reverse every word, but the words should stay in their places.
# 
# Input:A string.
# 
# Output:A string.
# 
# Precondition:The line consists only from alphabetical symbols and spaces.
# 
# 
# END_DESC

import re
def backward_string_by_word(text: str) -> str:
    text1 = re.findall(r'\w+', text)
    for i in text1:
        text = text.replace(i, i[::-1])
    return text