"""
Ashley Piccone 

Euler Problem #37: Truncatable primes
"""

from sympy import sieve

primes = [i for i in sieve.primerange(0, 10**6)]

def left_trunc(string):
    if (int(string) in primes):
        if (len(string) == 1):
            return True   
        else:
            return left_trunc(string[1:])
    else:
        return False

def right_trunc(string):
    if (int(string) in primes):
        if (len(string) == 1):
            return True   
        else:
            return right_trunc(string[:len(string)-1])
    else:
        return False

sum_nums = 0
for i in primes:
    if(left_trunc(str(i)) == True and right_trunc(str(i)) == True):
        sum_nums += i
        
print(sum_nums)
        








