"""
Ashley Piccone

Euler Problem #52: Permuted multiples
"""

def is_permutation(num1,num2):
    string1 = str(num1)
    string2 = str(num2)
    if (len(string1) != len(string2)):
        return False
    digits = []
    for i in range(0,len(string1)):
        digits.append(string1[i])
    for j in range(0,len(string2)):
        if string2[j] not in digits:
            return False
        else:
            digits.remove(string2[j])
            if (len(digits) == 0):
                return True
            
found = False
i = 0
while (found == False):
    i += 1
    if (is_permutation(i, 2*i) and is_permutation(i,3*i) and is_permutation(i,4*i) and is_permutation(i,5*i) and is_permutation(i,6*i)):
        found = True
        break

print(i)