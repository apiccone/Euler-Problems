"""
Ashley Piccone

Euler Problem #25: 1000 digit Fibonacci number
"""

import math
import numpy as np 

def fib_the_fun_way(F_n):
    phi = float((1 + np.sqrt(5)) / 2)
    fib_index = math.ceil((F_n - 1 + math.log10(np.sqrt(5))) / math.log10(phi))
    return fib_index

limit = input("Enter the length of the Fibonacci number you want (not in scientific notation because apparently I can't handle that):")
print("The index of the first fibonacci number to contain",limit,"digits is",fib_the_fun_way(int(limit)))
