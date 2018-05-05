"""
Ashley Piccone

Euler Problem #56: Powerful digit sum
"""

def sum_digits(num):
    string = str(num)
    tot = 0
    for i in range(0,len(string)):
        tot += int(string[i])
    return tot

max_sum = 0
for a in range(1,100):
    for b in range(1,100):
        s = sum_digits(a**b)
        if (s > max_sum):
            max_sum = s
            
print(max_sum)



