#!/usr/bin/env checkio --domain=py run end-of-other

# For language training our Robots want to learn about suffixes.
# 
# In this task, you are given a set of words in lower case.    Check whether there is a pair of words, such that one word is the end of another (a suffix of another).    For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", so the result is True.
# 
# Input:Words as a set of strings.
# 
# Output:True or False, as a boolean.
# 
# Precondition:2 ≤ len(words) < 30
# all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)
# 
# 
# END_DESC

def checkio(words_set):
    for i in words_set:
        for j in words_set:
            if i != j and i == j[-len(i):len(j)]:
                return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio({"hello", "lo", "he"}))

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print("Done! Time to check!")