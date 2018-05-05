"""
Ashley Piccone

Euler Problem #34: Digit factorials
"""

def factorial(num):
    fact = 1
    if (num == 1 or num == 2):
        return num
    for i in range(1,num+1):
        fact *= i
    return fact

sum_tot = 0
for i in range(3,10**5):
    string = str(i)
    fact_sum = 0
    for j in range(0,len(string)):
        fact_sum += factorial(int(string[j]))
    if (fact_sum == i):
        sum_tot += i

print(sum_tot)



