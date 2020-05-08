#!/usr/bin/env checkio --domain=py run number-factory

# You are given a two or more digits numberN.    For this mission, you should find the smallest positive number ofX,    such that the product of its digits is equal to N.    If X does not exist, then return 0.
# 
# Let's examine the example. N = 20. We can factorize this number as 2*10, but 10 is not a digit.    Also we can factorize it as 4*5 or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.
# 
# Hints:Remember prime numbers (numbers divisible by only one) and be careful with endless loops.
# 
# Input:A number N as an integer.
# 
# Output:The number X as an integer.
# 
# How it is used:This task will teach you how to work with numbers in code.    You can factorize numbers and reconstruct them into new numbers.    Of course you can solve this problem with brute force,    but is that the best way?    Numbers are the foundation of mathematics and programming.
# 
# Precondition:
# 9 < N < 105.
# 
# 
# END_DESC

def gen_prime_num(limit):
    for i in range (2, limit):
        celoe = True
        for j in range (2, (i+2)//2):
            if i % j == 0:
                celoe = False
                break
        if celoe:
            yield i




def checkio(number):
    x = list(range(2,10))
    x1 = list(gen_prime_num(number))
    #print(x1)
    sol, sol1=[], []
    
    def check (data):
        if (data in x):
            
            return data
        elif data > 10 and data in x1:
            return 0            
        else:
            z1 = ''
            for i in x:
                if (data/i).is_integer():
                    if i in x and data//i in x:
                        return int(str(i)+str(check(data//i)))
                    else:
                        z1 = (int((str(i)+str(check(data//i)))))
            print(z1)
            return z1
            
            
    #print (check(number))
    sol = check(number)
    
    
    if sol and not ('0' in str(sol)) :
        #print(sol)
        if sol < 10 and number > 81:
            return 0
        else:
            sol = list(i for i in str(sol))
            sol.sort()
            sol = int(''.join(sol))
            return sol
    else:
        #print(0)
        return 0
    

    
print(111, checkio(3125))
print(222, checkio(33))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"