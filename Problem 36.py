"""
Ashley Piccone

Euler Proble #36: Double base palindromes
"""

import numpy as np

def binary(num):
    string = []
    q = int(num)
    while (q >= 1):
        # add the remainder (0 or 1) to the string
        string.append(np.floor(q % 2))
        q = q / 2   
    # reverse the order
    return string[::-1]

def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False
    
# this function is from a previous hw
def is_palindrome(word):
    pal = False
    if (is_even(len(word))):
        for i in range(0,len(word)):
            if (word[i] == word[len(word)-i-1]):
                pal = True
            else:
                pal = False
                break
    else:
        for i in range(0,len(word)):
            if (i == int(len(word)/2) + 1):
                continue                     
            if (word[i] == word[len(word)-i-1]):
                pal = True
            else:
                pal = False
                break
    return pal
            
sum_pals = 0
for i in range(1,10**6):
    if (is_palindrome(str(i)) == True and is_palindrome(binary(i)) == True):
        sum_pals += i
print("The sum of numbers from 1 to 10**6 that are double base palindromes is:",sum_pals)

