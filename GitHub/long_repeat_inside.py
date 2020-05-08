#!/usr/bin/env checkio --domain=py run long-repeat-inside

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# It is the fourth and the last mission of the series. But if in the first mission you needed to find repeating letters, then in this one you should find a repeating sequence inside the substring. I have an example for you: in a string "abababc" - "ab" is a sequence that repeats more than once, so the answer will be "ababab"
# 
# Input:String.Output:String.
# 
# 
# END_DESC

def repeat_inside(line):
    """
        first the longest repeating substring
    """
    n_min, line1 = 1, ''
    for i in range(0, len(line)-1):
        for j in range(i+1, len(line)):
            x=line.count(line[i:j])
            for ins in range(x,1,-1):
                    #print(ins, line[i:j])
                    if line[i:j]*ins in line and len(line[i:j]*ins) >  n_min:
                        
                        print('+++', line[i:j]*ins)
                        n_min = len(line[i:j]*ins)
                        line1 = line[i:j]*ins
                        print('---', n_min, line1, ins, line )
                        break
            
            
            #print(line[i:j])
            #if  x > n_min:
                
    return line1

repeat_inside('abcabcabab')

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')