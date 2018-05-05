"""
Ashley Piccone

Euler Problem #21: Amicable numbers
"""

def proper_divisors(num):
    arr = []
    for i in range(1,int(num/2) + 1):
        if(num % i == 0):
            arr.append(i)
    return sum(arr)


def amicable_pairs(low,high):
    divisors = [proper_divisors(i) for i in range(low,high + 1)]
    pairs = []
    for i in range(high - low + 1):
        index = divisors[i] # grab the divisor sum for a number i and compare to possible matches
        if ((i + low < index) and (low <= index) and (index <= high) and (divisors[index - low] == i + low)):
            pairs.append([i+low,index])
    return pairs

pairs = amicable_pairs(1,10000)
sum_pairs = sum([sum(i) for i in pairs])
print(sum_pairs)













