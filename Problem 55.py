"""
Ashley Piccone

Euler Problem #55: Lychrel numbers
"""


def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False
    
def is_palindrome(word):
    pal = False
    if (is_even(len(word))):
        for i in range(0,len(word)):
            if (word[i] == word[len(word)-i-1]):
                pal = True
            else:
                pal = False
                break
    else:
        for i in range(0,len(word)):
            if (i == int(len(word)/2) + 1):
                continue                     
            if (word[i] == word[len(word)-i-1]):
                pal = True
            else:
                pal = False
                break
    return pal

tot = 0
for i in range(1,10**4):
    ly = True
    num = 1
    s = str(i)
    while (ly == True and num < 50):
        num += 1
        s = str(int(s) + int(s[::-1]))
        if (is_palindrome(s)):
            ly = False
            break
        if (num >= 50):
            ly = True 
            tot += 1
            break
    
print(tot)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    