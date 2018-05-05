"""
Ashley Piccone

Euler Problem #35: Circular primes
"""

from sympy import primerange

primes = set([i for i in primerange(1, 10**6)])

def permute(num):
    ret = False
    string = str(num)
    # permute the string
    for i in range(0,len(string)-1):
        string = string[1:] + string[0]
        val = int(string)
        if val not in primes:
            ret = False
            break
        else:
            ret = True
    return ret

count = 4
for i in primes:
    if (permute(i) == True):
        count += 1
        
print(count)
        










