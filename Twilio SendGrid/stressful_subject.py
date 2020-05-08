#!/usr/bin/env checkio --domain=py run stressful-subject

# 
# END_DESC

def is_stressful(subj):
    """
        recognize stressful subject
    """
    a, x = '', 0
    
    if subj[len(subj)-3:len(subj)] == '!!!':
        
        return True
    elif subj.isupper():
        return True
    subj = subj.lower() 
    
    for i in subj:
        if i.isalpha():
            a += i
            if len(a) > 1 and a[len(a)-1] == a[len(a)-2]:
                a = a[:len(a)-1]
    
    if a.find('help') != -1 or a.find('asap') != -1 or a.find('urgent') != -1:
        return True
    else:
        return False
            
    
is_stressful("where are you?!!!!")
if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')