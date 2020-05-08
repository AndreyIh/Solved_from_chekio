#!/usr/bin/env checkio --domain=py run largest-histogram

# "Your power to choose can never be taken from you.
# It can be neglected and it can be ignored.
# But if used, it can make all the difference."
# ― Steve Goodier
# 
# You have a histogram. Try to find size of the biggest rectangle you can build out of the histogram bars.
# 
# Input:List of all rectangles heights in histogram
# 
# Output:Area of the biggest rectangle
# 
# Example:
# 
# 
# largest_histogram([5]) == 5
# largest_histogram([5, 3]) == 6
# largest_histogram([1, 1, 4, 1]) == 4
# largest_histogram([1, 1, 3, 1]) == 4
# largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
# How it is used:There is no way the solution you come up with will be any useful in a real life. Just have some fun here.
# 
# Precondition:
# 0 < len(data) < 1000
# 
# 
# 
# END_DESC

def largest_histogram(histogram):
    max_h = 0
    for i in range(len(histogram), 0, -1):
        for j in range (len(histogram) - i, len(histogram)):
            z = histogram[len(histogram) - i: j+1]
            s = len(z)  * min(z)
            if s > max_h:
                max_h = s
    return max_h