#!/usr/bin/env checkio --domain=py run number-length

# You have a positive integer. Try to find out how many digits it has?
# 
# Input:A positive Int
# 
# Output:An Int.
# 
# 
# END_DESC

def number_length(a: int) -> int:
    return len(str(a))