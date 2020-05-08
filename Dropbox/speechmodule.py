#!/usr/bin/env checkio --domain=py run speechmodule

# Stephen's speech module is broken.    This module is responsible for his number pronunciation.    He has to click to input all of the numerical digits in a figure,    so when there are big numbers it can take him a long time.    Help the robot to speak properly and increase his number processing speed by writing a new speech module for him.    All the words in the string must be separated by exactly one space character.    Be careful with spaces -- it's hard to see if you place two spaces instead one.
# 
# Input:A number as an integer.
# 
# Output:The string representation of the number as a string.
# 
# How it is used:This concept may be useful for the speech synthesis software or automatic reports systems.    This system can also be used when writing a chatbot by assigning words or phrases numerical    values and having a system retrieve responses based on those values.
# 
# Precondition:0 < number < 1000
# 
# 
# END_DESC

def checkio(number):
    dictM = {1:{0:'zero ', 1:'one ', 2:'two ', 3:'three ', 4:'four ', 5:'five ',
            6:'six ', 7:'seven ', 8:'eight ', 9:'nine ', 10:'ten ',
            11:'eleven ', 12:'twelve ', 13:'thirteen ', 14:'fourteen ',
            15:'fifteen ', 16:'sixteen ', 17:'seventeen ', 18:'eighteen ',
            19:'nineteen ', 20:'twenty ', 30:'thirty ', 40:'forty ', 50:'fifty ',
            60:'sixty ', 70:'seventy ', 80:'eighty ', 90:'ninety '},
            3:{100:'hundred ', 1:'thousand ', 2:'million ',3:'billion ', 0:''}}
    money = str(number)
    money = ''.join(money.split())        # на всякий случай убираем пробелы
    n = 0
    dolar, dolar1 = '', ''
    a = []
    x = len(money)
    
    for i in range(x,0,-3):             # разбитие левой части числа на разряды
        z = i - 3
        if z < 0:
            z = 0
        a.append(money[z:i])

    for j in a:                         # перевод в буквы левой части суммы
        a1 = ''
        if len(j) == 3:
            a = int(j[0])
            b = int(j[1:3])
        else:
            a = 0
            b = int(j[0:len(j)])
        if a > 0:
            a1 = dictM[1][a] + dictM[3][100] 
        if (b <= 20 or b % 10 == 0) and b != 0:
            b = dictM[1][b]
        elif a > 0 and b == 0:
            b = ''
        else:
            b = dictM[1][(b // 10) * 10] + dictM[1][(b % 10)]
        dolar = a1 + b + dictM[3][n]
        dolar1 = dolar + dolar1
        n += 1

    #replace this for solution
    return dolar1.strip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')