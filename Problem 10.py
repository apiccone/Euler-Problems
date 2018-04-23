"""
Ashley Piccone

Euler Problem #10: Summation of Primes
"""
import sympy
import numpy as np

prime_set = set(sympy.sieve.primerange(0,2*10**6))

tot = 0
for i in range(0,2*10**6):
    if (i in prime_set):
        tot += i
    
print(tot)