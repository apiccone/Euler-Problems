"""
Ashley Piccone

Euler Problem #33: Digit cancelling fractions
"""

nums = set()
for i in range(10,100):
    for j in range(10,100):
        si = str(i)
        sj = str(j)
        if '0' in si or '0' in sj:
            continue
        if (i == j):
            continue
        
        if (si[0] == sj[0]):
            if (float(int(si[1]) / int(sj[1])) == float(i/j) and float(i/j) <= 1):
                nums.add(float(i/j))
                print(i,'/',j)
                
        elif (si[1] == sj[0]):
            if (float(int(si[0]) / int(sj[1]))  == float(i/j) and float(i/j) <= 1):
                nums.add(float(i/j))
                print(i,'/',j)
                        
        elif (si[0] == sj[1]):
            if (float(int(si[1]) / int(sj[0]))  == float(i/j) and float(i/j) <= 1):
                nums.add(float(i/j))
                print(i,'/',j)
            
        elif (sj[1] != 0 and si[1] == sj[1]):
            if (float(int(si[0]) / int(sj[0]))  == float(i/j)and float(i/j) <= 1):
                nums.add(float(i/j))
                print(i,'/',j)

print(16*19*26*49)

print(64*95*65*98)

