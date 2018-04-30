"""
Ashley Piccone

Euler Problem #5: Smallest Multiple
"""

def smallestmultiple(num):
    found = False
    val = 2
    while (found == False):
        # while the value hasn't been found
        for j in range(2,num):
            # if the remainder of dividing the value by each j is not zero
            # then test the next value
            if (val % j != 0):
                val += 1
                break
        else:
            # if the remainder of dividing the value by each j is zero
            # return that value
            found = True
            break
    return val

print ( "Problem 3: The smallest number that is a multiple of 1-20 is", smallestmultiple(20))
