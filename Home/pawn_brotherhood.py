#!/usr/bin/env checkio --domain=py run pawn-brotherhood

# 
# END_DESC

def safe_pawns(pawns: set) -> int:
    dict1 = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
    a, a1=[], 0
    for i in range(0, 8):
        a.append([])
        for j in range(0, 8):
            a[i].append(0)
    for p in pawns:
        l, m = p[0], int(p[1])
        a[m-1][dict1.get(l)] = 1
    for i in range(1, 8):
        for j in range(0, 8):
            l, r = j, j
            if j == 0:
                l = j + 2
            if j == 7:
                r = j - 2        
            if a[i][j] == 1 and (a[i-1][l-1] or a[i-1][r+1]):
                a1+=1
    return a1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")