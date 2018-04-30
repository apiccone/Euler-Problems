"""
Ashley Piccone

Euler Problem #39: Integer right triangles
"""

max_count = 0
max_per = 0
for p in range(6, 1001, 2):
    count = 0
    for a in range(2, int(p/3) + 1):
        # new requirement for a right triangle
        if  (p*(p - 2*a) % (2*(p - a)) == 0): 
            count += 1
            if (count >= max_count):
                max_count = count
                max_per = p
 
print("The number of solutions is maximized for p =", max_per)