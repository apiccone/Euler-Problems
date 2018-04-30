"""
Ashley Piccone

Euler Problem #26: Reciprocal cycles
"""

print("Reciprocal Cycles")
num = 1
big = 1
for kk in range(3, 1000, 2): # steps of 2 because anything even will stop
    if (kk % 5 == 0): # if kk is divisible by five, the digits stop
        continue
    m = 1
    while ((10 ** m) % kk != 1): # we want m to be as big as possible => more digits
        m += 1
    if (m > big):
        num = kk
        big = m
print ("The value d with the longest recurring cycle is",num)