"""
Ashley Piccone

Euler Problem #30: Digit fifth powers
"""

print("Digit Fifth Powers")
sum_nums = 0
for ii in range(2,10**6):
    string = str(ii) # convert number to a string to get the individual digits
    sum_digits = 0
    for jj in range(0,len(string)):
        sum_digits += int(string[jj])**5 # sum the fifth power of the digits
    if (sum_digits == ii): # if the sum is the number, add to sum_nums
        #print(ii,sum_digits)
        sum_nums += ii
print(sum_nums)