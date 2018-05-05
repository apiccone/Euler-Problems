"""
Ashley Piccone

Euler Problem #22: Name scores
"""

import codecs

file = codecs.open("Names_22.txt",'r','utf-8').read()

# make a dictionary to hold letter values
char_dict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

# sort alphabetically, remove all the "", and split the names with a comma
names = sorted(file.replace('"','').split(','), key=str)

val = 0
for i,j in enumerate(names):
	temp = 0
    # this loops through the letters in the word
	for k in j:
		temp += char_dict[k]
    # this multiples the word value (temp) by the word placement (i+1)
	val += temp * (i + 1)
	
print(val)
