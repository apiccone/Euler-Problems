"""
Ashley Piccone

Euler Problem #43: Sub-string divisibility
"""

from itertools import permutations

# too slow
#def pandigital(num):
#    ret = False
#    string = str(num)
#    nums = '1234567890'[:len(string)]
#    for i in range(0,len(string)):
#        if (string[i] in nums):
#            ret = True
#            nums = nums.replace(string[i],'')
#        else:
#            ret = False
#            break
#    return ret

def divisible(num):
    string = str(num)
    f2 = int(string[1] + string[2] + string[3])
    f3 = int(string[2] + string[3] + string[4])
    f5 = int(string[3] + string[4] + string[5])
    f7 = int(string[4] + string[5] + string[6])
    f11 = int(string[5] + string[6] + string[7])
    f13 = int(string[6] + string[7] + string[8])
    f17 = int(string[7] + string[8] + string[9])
    if (f2 % 2 == 0 and f3 % 3 == 0 and f5 % 5 == 0 and f7 % 7 == 0 and f11 % 11 == 0 and f13 % 13 == 0 and f17 % 17 == 0):
        return True
    else:
        return False

tot = 0
for i in permutations('0123456789'):
    if (i[0] == '0'):
        continue
    num = str()
    for j in range(0,len(i)):
        num += i[j]
    if (divisible(int(num)) == True):
        tot += int(num)
    
print(tot)
    
    
    
    
    
    
    
    
    