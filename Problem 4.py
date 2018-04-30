"""
Ashley Piccone

Euler Problem #4: Largest Palindrome Product
"""
import numpy as np
            
def palindrome(input_string):
    reverse_string = input_string[::-1]
    if input_string == reverse_string:
        return True
    else:
        return False
            
max_val = 0
for i in range(100,1000):
    for j in range(100,1000):
        prod = i * j
        if((prod > max_val) and (palindrome(str(prod)) == True)):
            max_val = i * j

print(max_val)









