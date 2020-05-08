#!/usr/bin/env checkio --domain=py run max-digit

# You have a number and you need to determine which digit in this number is the biggest.
# 
# Input:A positive int.
# 
# Output:An Int (0-9).
# 
# 
# END_DESC

def max_digit(number: int) -> int:
    return int(max([i for i in str(number)]))