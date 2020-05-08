#!/usr/bin/env checkio --domain=py run acceptable-password-v

# In this mission you need to create a password verification function.
# 
# Those are the verification conditions:
# 
# the length should be bigger than 6;should contain at least one digit, but it cannot consist of just digits;having numbers or containing just numbers does not apply to the password longer than 9.a string should not contain the word "password" in any case.Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

# Taken from mission Acceptable Password IV

def is_acceptable_password(password: str) -> bool:
    #a string should not contain the word "password" in any case.
    word = False if 'password' in password.lower() else True
    #should contain at least one digit -->
    dig = (sum([True for i in password if i.isdigit()]))
    # --> but it cannot consist of just digits; the length should be bigger than 6;
    #having numbers or containing just numbers does not apply to the password longer than 9.
    pas = (0 < dig < len(password) > 6 if len(password) < 10 else True)
    return pas and word