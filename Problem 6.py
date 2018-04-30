"""
Ashley Piccone

Euler Problem #6: Sum Square Difference
"""

import numpy as np

sum_squares = 0
for i in range(1,101):
    sum_squares += i**2

sum_nums = 0
for i in range(1,101):
    sum_nums += i
square_sum = sum_nums**2

print(square_sum-sum_squares)



