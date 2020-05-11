#!/usr/bin/env checkio --domain=py run counting-tiles

# Stephan needs some help building a circular landing zone using the ice square tiles for their new Ice Base.    Before he converts the area to a construction place, Stephan needs to figure out how many square tiles he will need.
# 
# Each square tile has size of 1x1 meters.     You need to calculate how many whole and partial tiles are needed for a circle with a radius of N meters.     The center of the circle will be at the intersection of four tiles. For example: a circle with a radius of 2 metres    requires 4 whole tiles and 12 partial tiles.
# 
# Input:The radius of a circle as a float
# 
# Output:The quantities whole and partial tiles as a list with two integers -- [solid, partial].
# 
# Precondition:
# 0 < radius ≤ 4
# 
# 
# 
# END_DESC

from math import ceil
def checkio(radius):
    """count tiles"""
    n, full, ch = ceil(radius), 0, 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i**2+j**2)**0.5 < radius:
                full += 1
            elif ((i-1)**2+(j-1)**2)**0.5 < radius and (i**2+j**2)**0.5 > radius:
                ch += 1
    return [full*4, ch*4]            
    
    
     

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #print(checkio(2))
    #print(checkio(3))
    print(checkio(2.1))
    print(checkio(4))
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"