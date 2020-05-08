#!/usr/bin/env checkio --domain=py run house-password

# 
# END_DESC

def checkio(parol):
    n = True
    a,b,c = 0,0,0
    for i in parol:
        if i.isdigit():
            a += 1
        if i.islower():
            b += 1
        if i.isupper():
            c += 1
    print(a,b,c,len(parol))
    if a == 0 or b == 0 or c ==0:
        n = False
    if len(parol) < 10:
        n = False
    
    #replace this for solution
    return n

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('ULFFunH8ni') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")