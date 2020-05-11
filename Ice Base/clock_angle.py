#!/usr/bin/env checkio --domain=py run clock-angle

# “The last clear thought I have is of my grandmother’s rust-colored wall clock ticking away        in the darkness of my apartment—my sanctuary where I dreamed and desired and hoped for        goodness and love. I wonder how long that clock will tick without anyone around to hear it.        I wonder if maybe I should have taken my grandmother’s silverware or jewelry instead. I        wonder – if I knew then what I know now – if I still would have approached Jade that first        night and invited her into my life, only to watch as she took it from me and fed it to some        Godless thing, as my mother had called it. Would I still have given myself over to her,        knowing it would end the same way, with the barbaric flicker of hope that this time she        could love me?”
# 
# ― J. Tonzelli, The End of Summer: Thirteen Tales of Halloween
# 
# Analog clocks display time with an analog clock face, which consists    of a round dial with the numbers 1 through 12, the hours in the day, around the outside.    The hours are indicated with an hour hand, which makes two revolutions in a day,    while the minutes are indicated by a minute hand, which makes one revolution per hour.    In this mission we will use a clock without second hand.    The hour hand moves smoothly and the minute hand moves step by step.
# 
# You are given a time in 24-hour format and you should calculate a lesser angle between    the hour and minute hands in degrees. Don't forget that clock has numbers from 1 to 12,    so 23 == 11. The time is given as a string with the follow format "HH:MM",    where HH is hours and MM is minutes. Hours and minutes are given in two digits format,    so "1" will be writen as "01".    The result should be given in degrees with precision ±0.1.
# 
# 
# 
# For example, on the given image we see "02:30" or "14:30" at the left part and    "01:42" or "13:42" at the right part. We need to find the lesser angle.
# 
# Input:A time as a string.
# 
# Output:The lesser angle as an integer or a float.
# 
# 
# Precondition:
# re.match("\A((2[0-3])|([0-1][0-9])):[0-5][0-9]\Z", time)
# 
# 
# END_DESC

def clock_angle(time):
    m, h = int(time[3:]), int(time[:2]) % 12
    minute, hour = round(m*6,1), round(h*30,1)+ round(m/2,1)
    return min(abs(minute-hour), 360-abs(hour-minute)) 
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"