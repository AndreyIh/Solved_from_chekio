#!/usr/bin/env checkio --domain=py run between-markers-simplified

# You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.
# 
# This is a simplified version of theBetween Markersmission.
# 
# The initial and final markers are always different.The initial and final markers are always 1 char size.The initial and final markers always exist in a string and go one after another.Input:Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
# 
# Output:A string.
# 
# Precondition:There can't be more than one final and one initial markers.
# 
# 
# END_DESC

def between_markers(a: str, b: str, c: str) -> str:
    """
        returns substring between two given markers
    """
    
    b = a.find(b) + 1
    c = a.find(c)
    if b == 0:
        b = 0
    if c == -1:
        c = len(a)
    if c < b:
        return ''
    else:
        return(a[b:c])

    


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')