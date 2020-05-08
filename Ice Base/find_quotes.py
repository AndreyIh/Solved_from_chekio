#!/usr/bin/env checkio --domain=py run find-quotes

# Your task at hand is to find all quotes in the text. And, as is already usual, do everything as quickly as possible :)You are given a string that consists of characters and a paired number of quotation marks. You need to  return an Iterable consisting  of the texts inside the quotation marks. But choose only quotes with double quotation marks ("). Single quotation marks (') aren’t appropriate.
# 
# Input:A string.
# 
# Output:An iterable.
# 
# 
# END_DESC

def find_quotes(a):
    a1, n1 = [], 0
    while a.find('"')>-1:
        if n1 % 2 == 1:
            a1.append(a[:a.find('"')])
        a = a[a.find('"')+1:]
        n1 += 1
    return a1


if __name__ == '__main__':
    print("Example:")
    print(find_quotes('"Greetings"'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_quotes('"Greetings"') == ['Greetings']
    assert find_quotes('Hi') == []
    assert find_quotes('good morning mister "superman"') == ['superman']
    assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']
    assert find_quotes('"Lorem Ipsum" is simply dummy text '
 'of the printing and typesetting '
 'industry. Lorem Ipsum has been the '
 '"industry\'s standard dummy text '
 'ever since the 1500s", when an '
 'unknown printer took a galley of '
 'type and scrambled it to make a type '
 'specimen book. It has survived not '
 'only five centuries, but also the '
 'leap into electronic typesetting, '
 'remaining essentially unchanged. "It '
 'was popularised in the 1960s" with '
 'the release of Letraset sheets '
 'containing Lorem Ipsum passages, and '
 'more recently with desktop '
 'publishing software like Aldus '
 'PageMaker including versions of '
 'Lorem Ipsum.') == ['Lorem Ipsum',
 "industry's standard dummy text ever "
 'since the 1500s',
 'It was popularised in the 1960s']
    assert find_quotes('count empty quotes ""') == ['']
    print("Coding complete? Click 'Check' to earn cool rewards!")