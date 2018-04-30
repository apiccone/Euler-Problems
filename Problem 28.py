"""
Ashley Piccone

Euler Problem #28: Number spiral diagonals
"""

print("Number Spirals")
n = int(input("Enter the length of your spiral (only one dimension):"))
start = 3
sum_num = 1 # start at one so we don't have to include this in the loops
step = 2
for ii in range(2,n+1,2): # tells how much to increment the inner loop by
    count = 0
    for jj in range(start,n**2+1,ii): # tells when to start and stop
        if (count < 4):
            sum_num += jj
            count += 1
        else:
            continue
        temp = jj 
    step += 2
    start = temp + step # resets the starting point
print("The sum of diagonals in your spiral is:",sum_num)
