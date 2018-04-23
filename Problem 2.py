"""
Ashley Piccone

Euler Problem #2: Even Fibonacci Numbers
"""
import numpy as np

def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False

def fibonacci(limit):
    val1 = 0
    val2 = 1
    fibs = []
    while (val1+val2 <= limit):
        fibs.append(val1+val2)
        temp = val1 + val2
        val1 = val2
        val2 = temp
    return fibs
        
fib_list = fibonacci(4*10**6)
tot = 0
for i in range(0,len(fib_list)):
    if (is_even(fib_list[i])):
        tot += fib_list[i]
        
print(tot)









