"""
Ashley Piccone

Euler Problem #42: Coded triangle numbers
"""

import codecs

file = codecs.open("Words_42.txt",'r','utf-8').read()

# make a dictionary to hold letter values
char_dict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

# sort alphabetically, remove all the "", and split the names with a comma
words = sorted(file.replace('"','').split(','), key=str)

vals = []
for i,j in enumerate(words):
	temp = 0
	for k in j:
		temp += char_dict[k]
	vals.append(temp)
	
triangle_nums = []
for n in range(1,100):
    triangle_nums.append(int(0.5 * n * (n-1)))

count = 0
for i in vals:
    if (i in triangle_nums):
        count += 1
        
print(count)





