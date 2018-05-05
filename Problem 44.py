"""
Ashley Piccone

Euler Problem #44: Pentagonal numbers
"""

import numpy as np

def pentagonal(num):
    n = (np.sqrt(24 * num + 1) + 1)/6
    if (n == int(n)):
        return True
    else:
        return False
    
res = 0
found = False
i = 1
while (found == False):
    i += 1
    n = n = i * (3 * i - 1) / 2
    for j in range(i-1,0,-1):
        m = j * (3 * j - 1) / 2
        if (pentagonal(n + m) == True and pentagonal(n - m) == True):
            res = n - m
            found = True
            break
    
print(res)
    









