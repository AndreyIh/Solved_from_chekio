#!/usr/bin/env checkio --domain=py run short-string-conversion

# You are given two strings, line1 and line2. Answer, what is the smallest number of operations you need to do in order to transform line1 into the line2?
# 
# Possible operations:
# 
# Delete one letter from one of the strings.Insert one letter into one of the strings.Replace one of the letters in one of the strings with another letter.
# 
# Input:Two arguments - two strings.
# 
# Output:An int, the minimum number of operations.
# 
# 
# Precondition:0<= len(line)<100
# 
# 
# END_DESC

def steps_to_convert(line1, line2):
    ns = abs(len(line2)-len(line1))
    maxl = ''
        
    for i in range(0, len(line2)-1):
        if line2[i] in line1:
            for j in range(i+1, len(line2)+1):
                if line2[i: j] in line1:
                    if len(line2[i: j]) > len(maxl):
                        maxl = line2[i: j]
                    else:
                        break
    
    return (max([len(line2), len(line1)]) - len(maxl))