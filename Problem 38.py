"""
Ashley Piccone

Euler Problem #38: Pandigital multiples
"""

def pandigital(num):
    ret = False
    string = str(num)
    
    digits = [1,2,3,4,5,6,7,8,9]
    digits = digits[:len(string)]
    
    for i in range(0,len(string)):
        if int(string[i]) in digits:
            ret = True
        else:
            ret = False
            break
        digits.remove(int(string[i]))
    return ret
        
# our number has to start with a 9, and it can only be multiplied by 2 to keep 9 digits
val = 0
for n in range(9487, 9213, -1):
    p = str(n*1) + str(n*2)
    if pandigital(p):
       val = p
       break

print(val)