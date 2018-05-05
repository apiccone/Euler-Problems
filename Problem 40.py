"""
Ashley Piccone

Euler Problem #40: Champernowne's constant
"""

string = str()
for i in range(1,10**6 + 1):
    string += str(i)
    
s = int(string[0]) * int(string[9]) * int(string[99]) * int(string[999]) * int(string[9999]) * int(string[99999]) * int(string[999999])
print(s)