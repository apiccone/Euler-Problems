"""
Ashley Piccone

Euler Problem #16: Sum of digits
"""


def sum_digits(num):
    # sums the value of the digits in a number by converting the num to a string
    string = str(num)
    tot = 0
    for i in range(0,len(string)):
        tot += int(string[i])
    return tot

print("The sum of the digits of 2^1000 is",sum_digits(2**1000))
