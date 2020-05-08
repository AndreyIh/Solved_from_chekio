#!/usr/bin/env checkio --domain=py run long-repeat

# There are four substring missionsthat were born all in one day and you shouldn’t need more than one day to solve them. All of these missions can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one, which makes it the answer.
# 
# Input:String.Output:Int.
# 
# 
# 
# 
# END_DESC

def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    a, b = 0, ''
    max0 = 0
    for i in line:
        if i == b:
            a += 1
        else:
            if a > max0:
                max0=a
            b = i
            a = 1
    if a > max0:
        max0=a        
    return max0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')