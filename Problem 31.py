"""
Ashley Piccone

Euler Problem #31: Coin sums
"""
import numpy as np

coins = [1,2,5,10,20,50,100,200]

val = 200

mat = np.zeros((201,8))
# add the only way to make 200 from 1p pieces
for p in range(0,val + 1):
    mat[p,0] = 1
     
for p in range(0,val + 1):
    # for each of our coins other than the 1p
    for c in range(1,8):
        # if the coin is big enough to fit other coins
        if (p >= coins[c]):
            # how this coin can be made of smaller coins
            mat[p, c] += mat[p, c-1]
            # what amount is left over
            mat[p, c] += mat[p-coins[c], c]
        # if it isn't big enough, use the smaller coins to make it
        else:
            mat[p, c] = mat[p, c-1]
            
print(mat[200,7])
       
       
       
       
      