#!/usr/bin/env checkio --domain=py run roman-numerals

# .numeral-table {    margin: auto;    border-collapse: collapse;    text-align: center;  }  .numeral-table * {    border: 1px solid black;    padding: 8px;    width: 50%;  }
# END_DESC

def checkio(num):
    num = str(num)
    dictV = {1:'I', 2:'V', 3:'X', 4:'L', 5:'C', 6:'D', 7:'M'}
    a1 = []
    for i in range(0, len(num)):
        n = int(num[i])
        l = (len(num)-i)*2
        if n == 5:
            a1.append(dictV[l]) 
        elif n % 5 <=3:
            if n // 5 < 1:
                a1.append(dictV[l-1]* (n % 5))
            if n // 5 == 1:
                a1.append(dictV[l]+dictV[l-1] * (n % 5))
        elif n % 5 == 4:
            if n // 5 < 1:
                a1.append(dictV[l-1] + dictV[l])
            if n // 5 == 1:
                a1.append(dictV[l-1] + dictV[l+1])
    a1 = ''.join(a1)
    return a1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')