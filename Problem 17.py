"""
Ashley Piccone

Euler Problem #17: Number letter counts
"""

import numpy as np

ones = []
ones.append('')
ones.append('one')
ones.append('two')
ones.append('three')
ones.append('four')
ones.append('five')
ones.append('six')
ones.append('seven')
ones.append('eight')
ones.append('nine')
ones.append('ten')
ones.append('eleven')
ones.append('twelve')
ones.append('thirteen')
ones.append('fourteen')
ones.append('fifteen')
ones.append('sixteen')
ones.append('seventeen')
ones.append('eighteen')
ones.append('nineteen')

tens = []
tens.append('twenty')
tens.append('thirty')
tens.append('forty')
tens.append('fifty')
tens.append('sixty')
tens.append('seventy')
tens.append('eighty')
tens.append('ninety')


def num_length(n):
    length = 0
    n = int(n)
    if (n < 100):
        if (n < 20):
            length = len(ones[n])
            if (n == 0):
                length -= 4
        else:
            length = len(tens[int(n / 10)-2] + ones[n % 10])
    else:
        thous = np.floor(n / 1000)
        hun = int(np.floor(n / 100) % 10)
        ten = n % 100
        if (n > 999):
            length += len('thousand') + num_length(thous)
        if (hun != 0):
            length += len('hundred') + len(ones[hun])
        if (ten != 0):
            length += len('and') + num_length(ten)
    return length
        
tot = 0    
for i in range(1,1001):
    tot += num_length(i)
    
print(tot)








