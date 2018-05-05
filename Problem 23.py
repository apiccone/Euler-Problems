"""
Ashley Piccone

Euler Problem #23: Non-abundant sums
"""

import numpy as np

def abundant(num):
    if (num < 12):
        return False
    
    divisors = []
    divisors.append(1)
    
    largest = int(np.sqrt(num))
    if (largest**2 == num):
        divisors.append(largest)
    else:
        largest += 1
    
    for i in range(2,largest):
        if (num % i == 0):
            divisors.append(i)
            divisors.append(num / i)
                       
    if (sum(divisors) > num):
        return True
    else:
        return False

abundant_list = []
for i in range(1,28124):
    if (abundant(i) == True):
        abundant_list.append(i)
abundant_set = set(abundant_list)

def abundant_sum(num):
    for i in abundant_list:
        if (i > num):
            return False
        if (num - i) in abundant_set:
            return True

val = 0
for i in range(1,28124):
    if (abundant_sum(i) == False):
        val += i
        
print(val)









