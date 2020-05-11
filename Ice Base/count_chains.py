#!/usr/bin/env checkio --domain=py run count-chains

# In this mission you must count chains.
# 
# You are given a list of details of the circle (tuple of X-coordinate, Y-coordinate, radius).
# You have to return the number of groups of circles where their circumferences intersect.
# 
# NOTE:
# 
# Only one circle counts as one group.
# 
# 
# END_DESC

from typing import List, Tuple

def pair (circle_1, circle_2):
    lenght = ((circle_1[0]-circle_2[0])**2+(circle_1[1]-circle_2[1])**2)**0.5
    return lenght < (circle_1[2]+circle_2[2]) and lenght>abs((circle_1[2]-circle_2[2]))

def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    lst, n, k = [], 0, range(len(circles))
    for i in range(len(circles)):
        for j in range(i+1, len(circles)):
            
            if pair(circles[i], circles[j]):
                lst.append(str(i)+'-'+str(j))
                
    circles_1 = circles[:]  #[(1, 1, 1), (2, 2, 1), (3, 3, 1)]
    while circles_1:
        first = circles_1.pop(0)
        print(circles_1,'**************')
        n+=1
        for i in range(len(circles)):
            if first != circles[i] and pair(first, circles[i]):
                if circles[i] in circles_1:
                    z = circles_1.pop(circles_1.index(circles[i]))
                    print(circles_1,'--------')
                    
                    for j in range(len(circles)):
                        if z != circles[j] and pair(z, circles[j]):
                            if circles[j] in circles_1:
                                u = circles_1.pop(circles_1.index(circles[j]))
                                print(circles_1,'++--------')
                                
                                for c in range(len(circles)):
                                    if u != circles[c] and pair(u, circles[c]):
                                        if circles[c] in circles_1:
                                            u = circles_1.pop(circles_1.index(circles[c]))
                                            print(circles_1,'++--------')
                
    
            
            
            
                
    
    return n


if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))
    print(count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]))
    print(count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]))
    print(count_chains([(2, 2, 1), (2, 2, 2)]))
    print(count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]))
    print(count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")