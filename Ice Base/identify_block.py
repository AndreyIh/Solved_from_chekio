#!/usr/bin/env checkio --domain=py run identify-block

# This mission uses a 4x4 grid. Each square is numbered from 1 to 16 in row-major order.
# You are given 4 numbers(a set of integers).These numbers represent the positions of each square on the grid and a whole block if all the squares are adjacent.
# 
# You have to identify the kind of block. (Refer to the following image or comment of initial code for the kind of block).
# The answer is an upper case alphabet letter ('I', 'J', 'L', 'O', 'S', 'T' or 'Z'). If it’s not a block, then return None.
# 
# The block is placed anywhere on the grid and can be rotated (0, 90, 180 or 270 degrees).
# 
# 
# 
# Input:4 numbers (a set of integers)
# 
# Output:the kind of block (an alphabet letter or         None)
# 
# 
# END_DESC

def identify_block(numbers):
    """
    grid(4x4):
    +--+--+--+--+
    |1 |2 |3 |4 |
    +--+--+--+--+
    |5 |6 |7 |8 |
    +--+--+--+--+
    |9 |10|11|12|
    +--+--+--+--+
    |13|14|15|16|
    +--+--+--+--+


    blocks(7 kinds):

    'I'  'J'  'L'  'O'  'S'  'T'  'Z'

     *    *   *    **    **  ***  **
     *    *   *    **   **    *    **
     *   **   **
     *

    """
    numbers = list(numbers)
    numbers.sort()
    if numbers[1] == numbers[0] + 1 and numbers[2] == numbers[0]+2 and numbers[3] == numbers[0]+3:
        return "I"
    elif numbers[1] == numbers[0] + 4 and numbers[2] == numbers[0]+8 and numbers[3] == numbers[0]+12:
        return "I"
        
    elif numbers[1] == numbers[0] + 4 and numbers[2] == numbers[0]+7 and numbers[3] == numbers[0]+8:
        return "J"
    elif numbers[1] == numbers[0] + 1 and numbers[2] == numbers[0]+4 and numbers[3] == numbers[0]+8:
        return "J"
    elif numbers[1] == numbers[0] + 1 and numbers[2] == numbers[0]+2 and numbers[3] == numbers[0]+6:
        return "J"
    elif numbers[1] == numbers[0] + 4 and numbers[2] == numbers[0]+5 and numbers[3] == numbers[0]+6:
        return "J"
        
    elif numbers[1] == numbers[0] + 4 and numbers[2] == numbers[0]+8 and numbers[3] == numbers[0]+9:
        return "L"
    elif numbers[1] == numbers[0] + 1 and numbers[2] == numbers[0]+5 and numbers[3] == numbers[0]+9:
        return "L"
    elif numbers[1] == numbers[0] + 2 and numbers[2] == numbers[0]+3 and numbers[3] == numbers[0]+4:
        return "L"
    elif numbers[1] == numbers[0] + 1 and numbers[2] == numbers[0]+2 and numbers[3] == numbers[0]+4:
        return "L"
    
    elif numbers[1] == numbers[0] + 1 and numbers[2] == numbers[0]+4 and numbers[3] == numbers[0]+5:
        return "O"
        
    elif numbers[1] == numbers[0] + 1 and numbers[2] == numbers[0]+3 and numbers[3] == numbers[0]+4:
        return "S"
    elif numbers[1] == numbers[0] + 4 and numbers[2] == numbers[0]+5 and numbers[3] == numbers[0]+9:
        return "S"
        
    elif numbers[1] == numbers[0] + 1 and numbers[2] == numbers[0]+5 and numbers[3] == numbers[0]+6:
        return "Z"
    elif numbers[0]%4 != 1 and numbers[1] == numbers[0] + 3 and numbers[2] == numbers[0]+4 and numbers[3] == numbers[0]+7:
        return "Z"
        
    elif numbers[1] == numbers[0] + 1 and numbers[2] == numbers[0]+2 and numbers[3] == numbers[0]+5:
        return "T"
    elif numbers[1] == numbers[0] + 3 and numbers[2] == numbers[0]+4 and numbers[3] == numbers[0]+5:
        return "T"
    elif numbers[1] == numbers[0] + 4 and numbers[2] == numbers[0]+5 and numbers[3] == numbers[0]+8:
        return "T"
    elif numbers[1] == numbers[0] + 3 and numbers[2] == numbers[0]+4 and numbers[3] == numbers[0]+8:
        return "T"
        
    return None

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2, 3, 7, 11}) == 'L', 'L'
    assert identify_block({4, 8, 12, 16}) == 'I', 'I'
    assert identify_block({3, 1, 5, 8}) == None, 'None'
    print('"Run" is good. How is "Check"?')