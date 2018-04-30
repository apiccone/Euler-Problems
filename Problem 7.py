"""
Ashley Piccone

Euler Problem #7: 10001st Prime Number
"""
import time

def prime_test(num):
    # determines if a number is prime
    arr = []
    for k in range(2,num):
        # for k from 2 until the user's entry num
        # append the remainder of dividing num by k
        arr.append(num % k)
    if (arr.count(0) == 0):
        # if that remainder is never zero, the num is prime
        return True
    else:
        return False
    
def find_primes(num):
    n = 12**5
    tick = time.time()
    multiples = []
    primes = []
    # for i until some number that we know is greater than the 10001st prime
    for i in range(2, n):
        if (len(primes) == num):
            # if our array is the nth prime long, break
            break
        if i not in multiples:
            # if i isn't in our list of multiples, add it
            primes.append(i)
            for j in range(i*i, n, i):
                # also add all the multiples of i from i**2 up until n
                # the multiples below i**2 are already included
                multiples.append(j)
    print("The ", num, "th prime is: ", primes[int(num)-1])
    tock = time.time()
    time_delta = float( tock - tick )
    print ("It took us exactly T ={} s to generate {} prime numbers ".format(time_delta,num))

nth = input("Enter what prime number you want.")
# if you want to use my sieve algorithm, it's up there but this works better
# find_primes(nth)   
# still gonna take about 5 minutes for 10001
time_0 = time.time()
nn = 1
tt = 3
while (nn < int(nth)):
    if (prime_test(tt) == True):
        nn += 1
    tt += 2
time_1 = time.time()
print("The ", nth, "th prime is: ", tt -2)
time_delta = float( time_1 - time_0 )
print ("It took us exactly T ={} s to generate {} prime numbers ".format(time_delta,tt - 2))
