#!/usr/bin/env checkio --domain=py run oil-pie

# 
# END_DESC

from math import gcd


def divide_pie(groups):
    x = sum(abs(i) for i in groups)
    lst = [x, x]

    for drones in groups:
        common = gcd(drones, x)
        print(common)
        current = [drones//common, x//common]

        if current[0] > 0:
            lst[0] = lst[0]*current[1] - current[0]*lst[1]
            lst[1] *= current[1]

        if current[0] < 0:
            lst[0] *= current[0] + current[1]
            lst[1] *= current[1]

        common = gcd(int(lst[0]), int(lst[1]))
        lst[0] //= common
        lst[1] //= common

    return tuple(lst)


if __name__ == '__main__':
    print(tuple(divide_pie((2, -1, 3))))
    print(tuple(divide_pie((2, -1, 3))))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"