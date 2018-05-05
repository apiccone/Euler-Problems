"""
Ashley Piccone

Euler Problem #29: Distinct powers
"""

seq = set()
for i in range(2,101):
    for j in range(2,101):
        seq.add(i**j)
        
print(len(seq))










