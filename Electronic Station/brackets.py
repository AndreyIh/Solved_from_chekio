#!/usr/bin/env checkio --domain=py run brackets

# “Great!” Exclaimed Sofia. “Now we have the password.”
# 
# “To what exactly?” Quipped Nikola.
# 
# “Untold treasures, vast riches beyond belief! Gold! Silver! Silicon! Hydraulic Fluid! Anything your heart        desires!”
# 
# “And you’re going to do what with a password to absolutely nothing?” Nikola smirked.
# 
# “Oh... Right...”
# 
# Stephen spoke up. “Well, this door back here has a keypad. Only thing is the brackets look pretty busted up. We        could try fixing it and then punching in the password?”
# 
# “YES! That!” Sofia exclaimed.
# 
# You are given an expression with numbers, brackets and operators.    For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]".    Brackets are used to determine scope or to restrict some expression.     If a bracket is open, then it must be closed with a closing bracket of the same type.     The scope of a bracket must not intersected by another bracket.     In this task you should make a decision, whether to correct an expression or not based on the brackets.     Do not worry about operators and operands.
# 
# Input:An expression with different of types brackets as a string (unicode).
# 
# Output:A verdict on the correctness of the expression in boolean (True or False).
# 
# Precondition:
# There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
# 0 < len(expression) < 103
# 
# 
# END_DESC

import re

def checkio(expr):
    expr = re.sub('[0-9+\-*/]','',expr)
    print(expr)
    while len(expr) > 0:
        expr1 = expr
        expr = re.sub( '(\[])|(\{})|(\(\))', '', expr)
        if expr1 == expr:
            break
    if len(expr) == 0:
        return True
    else:
        return False
   
    
        
        
checkio("[1+202]*3*({4+3)}")            
            
"""
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem" 
    f1 = r"[(](?!\")(?!\{)(?!\[)[\d\*\-\+\/]*[)]"
    f2 = r"[\{](?!\")(?!\{)(?!\[)[\d\*\-\+\/]*[\}]"
    f3 = r"[\[](?!\")(?!\{)(?!\[)[\d\*\-\+\/]*[\]]"
    f = [f1, f2, f3]
    f4 = r"[{([})\]]"
    n1 = len(re.findall(f4, expr))
    if n1 % 2 == 1:
        return False
        
    while n1 > 0:
        expr1 = expr
        for i in f:
            expr = re.sub(i, '', expr, count=0)
        if expr1 == expr:
            break
        
        # print(expr)
    
    
    n1 = len(re.findall(f4, expr))
    # print(n1)
    if n1 == 0:
        return True
    else:
        return False
    """