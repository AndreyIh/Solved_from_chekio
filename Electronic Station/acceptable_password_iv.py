#!/usr/bin/env checkio --domain=py run acceptable-password-iv

# In this mission you need to create a password verification function.
# 
# Those are the verification conditions:
# 
# the length should be bigger than 6;should contain at least one digit, but it cannot consist of just digits;having numbers or containing just numbers does not apply to the password longer than 9.Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

def is_acceptable_password(password: str) -> bool:
    dig = (sum([True for i in password if i.isdigit()]))
    return 0 < dig < len(password) > 6 if len(password) < 10 else True