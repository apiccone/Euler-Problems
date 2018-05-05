"""
Ashley Piccone

Euler Problem #63: Powerful digit counts
"""

from math import log10
# 10**n is always n+1 digits long

def num_digits(num):
    return int(log10(num))+1

val = 0
for n in range(1, 10):
    # limit is the max val where there are n digits in n**limit
    limit = int(1 / (1 - log10(n)))
    val += limit
        
print(val)