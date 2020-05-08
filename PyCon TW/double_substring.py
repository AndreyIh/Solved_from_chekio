#!/usr/bin/env checkio --domain=py run double-substring

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# This is the third mission of the series, and it’s the only one where you have to return not a substring but a substring length. You need to find a substring that repeats more than once in a given string. This reiteration shouldn't have overlaps. For example, in a string "abcab" the longest substring that repeats more than once is "ab", so the answer should be 2 (length of "ab")
# 
# Input:String.Output:Int.
# 
# 
# 
# 
# END_DESC

def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    max_l, n, m = 0, 0, 0
    a = []
    for i in line:
        while line.count(i) > 1:
            if n + len(i) < len(line):
                i += line[n + len(i)]
            else:
                i += '1'
        m = len (i) - 1       
        n += 1
        # print(m, n, 100500)
        if m and m > max_l:
            max_l = m
            print('max', max_l)
            
            
            
    return max_l
    
double_substring('aghtfghkofgh')

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')