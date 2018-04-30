"""
Ashley Piccone

Euler Problem #9: Special Pythagorean Triplet
"""

def pyth_trip(a, b, c):
    if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
        # if two of the numbers each squared add to the third squared, return true
        return True
    else:
        return 
    
print("The Pythagorean triplet that adds to 1000 is")
found = False
while (found == False):
    for i in range(1,500):
        if (found == False):
            for j in range(1,500):
                if (found ==False):
                    for k in range(1,500):
                        if (i+j+k==1000 and pyth_trip(i,j,k)==True):
                            # if the numbers add to 1000 and the function returns true
                            print(i,j,k)
                            print("a * b * c =", i*j*k)
                            found = True
                            break
                