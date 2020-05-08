#!/usr/bin/env checkio --domain=py run date-and-time-converter

# Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
# Your task is simple - convert the input date and time from computer format into a "human" format.
# 
# 
# 
# Input:Date and time as a string
# 
# Output:The same date and time, but in a more readable format
# 
# Precondition:
# 0<date<= 31
# 0<month<= 12
# 0<year<= 3000
# 0<hours<24
# 0<minutes<60
# 
# 
# END_DESC

import datetime 

def date_time(time: str) -> str:
    d = datetime.datetime.strptime(time[0:10], '%d.%m.%Y').date()
    d = d.strftime("%d %B %Y") if d.strftime("%d %B %Y")[0] != '0' else d.strftime("%d %B %Y")[1:]
    d1, d2 = int(time[11:13]), int(time[14:16])
    z1 = 'hour' if d1 == 1 else 'hours'
    z2 = 'minute' if d2 == 1 else 'minutes'
    return f'{d} year {d1} {z1} {d2} {z2}'


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")