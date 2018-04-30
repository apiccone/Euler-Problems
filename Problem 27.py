"""
Ashley Piccone

Euler Problem #27: Quadratic primes
"""

import sympy

print("Quadratic Primes")
max_n = 0
a_val = 0
b_val = 0
# generate a list of primes to look through
prime_set = set(sympy.sieve.primerange(0,10000))
for a in range(-999,1000):
    for b in range(-1000,1001):
        n = 0
        # if this quadratic is in the primes, keep increasing n
        while ((n**2 + a*n + b) in prime_set):
            n += 1
        # when n is a max, store it
        if (n-1 > max_n):
            a_val = a
            b_val = b
            max_n = n
print("The greatest product of", a_val,"and",b_val,"is",a_val*b_val)