#!/usr/bin/env checkio --domain=py run remove-accents

# Assuming you are developing a user based system like facebook, you will want to provide the functionality to search for other members regardless of the presence of accents in a username. Without using a 3rd party collation library, you will need to remove the accents from the username before the comparison.
# 
# é - letter with an accent; e - letter without an accent; ̀ and ́ - the stand alone accents;
# 
# 
# 
# Input:A phrase as a string (unicode).
# 
# Output:An accent free Unicode string.
# 
# How it is used:It might be a part of a username verification process or a system that proposes the username based on the first and last name of a user.
# 
# Precondition:0≤|input|≤40
# 
# 
# END_DESC

import unicodedata
def checkio(in_string):
    z = ''
    for i in in_string:
        n = unicodedata.name(i)
        print(unicodedata.name(i))        
        if n[0:11] == 'LATIN SMALL':
            z+=unicodedata.lookup(n[0:20])
        elif n[0:13] == 'LATIN CAPITAL':
            z+=unicodedata.lookup(n[0:22])
        elif n[0:9] == 'COMBINING':
            pass
        else:
            z+=i
        #print(unicodedata.name(i))
    print(z)
    #print(z.lower())
        

#>>> unicodedata.lookup("EURO SIGN")
#'€'
    
    
    
    
    return z
    

checkio(u"àèìǹòùẁỳÀÈÌǸÒÙẀỲ")

checkio(u"loài trăn lớn")

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')