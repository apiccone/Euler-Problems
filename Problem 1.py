"""
Ashley Piccone

Euler Problem 1: Multiples of 3 and 5
"""

def multiples():
    sum = 0
    for x in range(1,1000):
        # for all the numbers between 1 and 1000
        # if divisible by 3 and 5, add to the total sum
        if x%3==0 or x%5==0:
            sum = sum + x
    return sum     

print ( "Problem 1: The sum of the multiples of both 3 and 5 below 100 is",multiples())