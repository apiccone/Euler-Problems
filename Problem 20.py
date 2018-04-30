"""
Ashley Piccone

Euler Problem #20: Factorial digit sum
"""

def factorial(num):
    # computes the factorial of a number
    product = 1
    for i in range(2,num):
        product = product * i
    return product

def sum_digits(num):
    # sums the value of the digits in a number by converting the num to a string
    string = str(num)
    tot = 0
    for i in range(0,len(string)):
        tot += int(string[i])
    return tot

print("The sum of the digits of 100! is", sum_digits(factorial(100)))
