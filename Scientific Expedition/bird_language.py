#!/usr/bin/env checkio --domain=py run bird-language

# Stephan has a friend who happens to be a little mechbird.    Recently, he was trying to teach it how to speak basic language.    Today the bird spoke its first word: "hieeelalaooo".    This sounds a lot like "hello", but with too many vowels.    Stephan asked Nikola for help and he helped to examine how the bird changes words.    With the information they discovered, we should help them to make a translation module.
# 
# The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);Vowels letters == "aeiouy".
# You are given an ornithological phrase as several words which are separated by white-spaces    (each pair of words by one whitespace).    The bird does not know how to punctuate its phrases and only speaks words as letters.    All words are given in lowercase.    You should translate this phrase from the bird language to something more understandable.
# 
# Input:A bird phrase as a string.
# 
# Output:The translation as a string.
# 
# Precondition:re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
# A phrase always has the translation.
# 
# 
# END_DESC

VOWELS = "aeiouy"

def translate(phrase):
    t = phrase.split()
    t1=[]
    
    for i in t:
        
        j = 0
        while j < len(i)-1:
            
            if i[j] not in list(['a', 'e', 'i', 'o', 'u', 'y']):
                i = i[0:j+1] + i[j+2:len(i)]
            j += 1
            
        n = 2
        while n < len(i):
            if i[n] == i[n-1] and i[n]== i[n-2]:
                    i = i[0:n-2] + i[n:len(i)]
            n+=1
            
                
                
        t1.append(i)
            
    t1 = ' '.join(t1)
    print (t1)
    return t1


if __name__ == '__main__':
    print("Example:")
    print(translate("hoooowe yyyooouuu duoooiiine"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")