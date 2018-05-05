"""
Ashley Piccone

Euler Problem #24: Lexigraphic permutations
"""

from itertools import permutations

perm = sorted(list(permutations('0123456789')))

print(perm[10**6 - 1])







