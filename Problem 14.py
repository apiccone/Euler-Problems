"""
Ashley Piccone

Euler Problem #14: Longest Collatz sequence
"""

def collatz_seq(n):
    arr = []
    while (n > 1):
        if (n % 2 == 0):
            n = n / 2
        else:
            n = 3*n + 1 
        arr.append(n)
    return len(arr) + 1

print(collatz_seq(13))

max_length = 0
num = 0
for i in range(0,10**6):
    if (collatz_seq(i) > max_length):
        max_length = collatz_seq(i)
        num = i

print(num)





















