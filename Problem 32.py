"""
Ashley Piccone

EUler Problem #32: Pandigial products
"""

print("Pandigital Products")
digits = set('123456789')
products = set() # using a set removes duplicates
# we want to loop through the multiplicands with one digit first
for jj in range(9):
	for kk in range(999,9999):
		dig_string = str(jj)+str(kk)+str(jj*kk)
		if (len(dig_string) == 9 and set(dig_string) == digits):
			products.add(jj*kk)
# now let's do the two digit ones
for ll in range(9,99):
	for nn in range(99,999):
		dig_string = str(ll)+str(nn)+str(ll*nn)
		if (len(dig_string) == 9 and set(dig_string) == digits):
			products.add(ll*nn)
sum_prod = 0
# summing all of the products in our set
for mm in products:
    sum_prod += mm
print(sum_prod)

