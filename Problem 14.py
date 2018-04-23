"""
Ashley Piccone

Euler Problem #14: Longest Collatz sequence
"""

n = 13
seq_len = 0
start = 0

#for i in range(1,n):
#    j = i
seq = []
j = 3
while (j >= 1):
    if (j % 2 == 0):
        seq.append(j/2)
        j = j/2
    else:
        seq.append(3*j + 1)
        j = 3*j + 1
#if (len(seq) > seq_len):
#    seq_len = len(seq)
#    start = i

print(seq)





















