"""
Ashley Piccone 

Euler Problem 3: Largest Prime Factor
"""

import numpy as np

def prime_test(num):
    # determines if a number is prime
    arr = []
    for k in range(2,num):
        # for k from 2 until the user's entry num
        # append the remainder of dividing num by k
        arr.append(num % k)
    if (arr.count(0) == 0):
        # if that remainder is never zero, the num is prime
        return True
    else:
        return False
    
n = np.long(600851475143)
arr = []
for k in range(2,int(np.sqrt(n)+1)):
    if (n % k == 0 and prime_test(k) == True):
        arr.append(k)
print ( "Problem 2: The greatest prime factor of 600851475143 is", arr[-1])