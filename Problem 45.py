"""
Ashley Piccone

Euler Problem #45: Triangular, pentagonal and hexagonal
"""

import numpy as np

def pentagonal(num):
    n = (np.sqrt(24 * num + 1) + 1)/6
    if (n == int(n)):
        return True
    else:
        return False
    
# all triangular numbers are hexagonal, so we only need to check the hexagonal ones
for i in range(0,10**5):
    hex_num = i * (2*i - 1)
    if (pentagonal(hex_num) == True):
        print(hex_num)
    











