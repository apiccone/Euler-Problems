"""
Ashley Piccone

Euler Problem #12: Highly divisible triangular number
"""
import numpy as np

def num_divisors(n):
    if (n % 2 == 0): #if n is even, split it in half
        n = n/2
    divisors = 1
    count = 0
    while (n % 2 == 0): # keep halving 
        count += 1
        n = n/2
    divisors = divisors * (count + 1) # add one for the number itself
    p = 3
    while (n != 1): # while we are odd but not one
        count = 0
        while (n % p == 0): # divide by odd factors
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors

def triangular_index(limit):
    n = 1
    lnum = num_divisors(n)
    rnum = num_divisors(n+1)
    while (lnum * rnum < limit):
        n += 1
        lnum, rnum = rnum, num_divisors(n+1)
    return n

index = triangular_index(500)
triangle = (index * (index + 1)) / 2
print(triangle)








