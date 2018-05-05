"""
Ashley Piccone

Euler Problem #41: Pandigital prime
"""

from sympy import sieve

primes_7 = [i for i in sieve.primerange(10**6,10**7)]

def pandigital(num):
    ret = False
    string = str(num)
    nums = '1234567890'[:len(string)]
    for i in range(0,len(string)):
        if (string[i] in nums):
            ret = True
            nums = nums.replace(string[i],'')
        else:
            ret = False
            break
    return ret

# we only need to check the four and seven digit primes because the others will be divisible by 3 if they have the 
# correct pandigital properties. Obviously the seven digit primes will be larger than the four, so I only check those
max_val = 0
for n in primes_7:
    if (pandigital(n) == True):
        if(n > max_val):
            max_val = n

print(max_val)