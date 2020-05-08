#!/usr/bin/env checkio --domain=py run triangle-angles

# You are given the lengths for each side on a triangle.    You need to find all three angles for this triangle.    If the given side lengths cannot form a triangle (or form a degenerated triangle),    then you must return all angles as 0 (zero).    The angles should be represented as a list of integers inascending order.    Each angle is measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).
# 
# 
# 
# Input:The lengths of the sides of a triangle as integers.
# 
# Output:Angles of a triangle in degrees as sorted list of integers.
# 
# Precondition:
# 0 < a,b,c ≤ 1000
# 
# 
# END_DESC

from math import *
from typing import List

def checkio(a: int, b: int, c: int) -> List[int]:
    trian, angl = [a, b, c], []
    trian.sort()
    if trian[0] + trian[1] > trian[2]:
        angl.append(round(degrees(acos((a**2+b**2-c**2)/(2*a*b))), 0))
        angl.append(round(degrees(acos((b**2+c**2-a**2)/(2*c*b))), 0))
        angl.append(round(degrees(acos((a**2+c**2-b**2)/(2*a*c))), 0))
        print(angl)
        angl.sort()
        print(angl)
    else:
        angl = [0, 0, 0]

    angl.sort()
    return angl
checkio(3, 4, 5)
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(3, 4, 5))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")