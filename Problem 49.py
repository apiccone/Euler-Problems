"""
Ashley Piccone

Euler Problem #49: Prime permutations
"""

from sympy import sieve

primes = [i for i in sieve.primerange(10**3,10**4)]

def is_permutation(num1,num2):
    string1 = str(num1)
    string2 = str(num2)
    if (len(string1) != len(string2)):
        return False
    digits = []
    for i in range(0,len(string1)):
        digits.append(string1[i])
    for j in range(0,len(string2)):
        if string2[j] not in digits:
            return False
        else:
            digits.remove(string2[j])
            if (len(digits) == 0):
                return True

limit = 10**4
res = str()
for i in primes:
    for j in primes:
        k = j + (j - i)
        if (k < limit and k in primes and i != j and i != k and j != k):
            if (is_permutation(i,j) and is_permutation(i,k)):
                res = str(i) + str(j) + str(k)
                print(res)
    
    
    
    
    
    
    
    
    
    
    
    
    
