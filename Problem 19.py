"""
Ashley Piccone

Euler Problem #19: Counting Sundays
"""

import numpy as np

# gaussian formula
def day_of_week(day,month,year):
    if (month == 1 or month == 2):
        Y = year - 1
        m = month + 10
    else:
        Y = year
        m = month - 2
        
    y = int(str(Y)[2:])
    c = int(str(Y)[:2])

    w = (day + np.floor(2.6*m - 0.2) + y + np.floor(y/4) + np.floor(c/4) -2*c) % 7
    return w
    
count = 0
for y in range(1901,2001):
    for m in range(1,13):
        if(day_of_week(1,m,y) == 0.0):
            count += 1
            
print(count)
        
        