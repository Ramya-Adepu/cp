# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math
def kaprekar(n):
    if n==1:
        return True
    sq = n*n
    countd = 0
    while not sq == 0 :
        countd = countd + 1
        sq = sq // 10
    sq = n*n 
    d = 0
    while(d < countd):
        d = d + 1
        eq_parts = int(math.pow(10,d))
        if eq_parts == n :
            continue
        sum = (sq//eq_parts) + (sq % eq_parts)
        if sum == n :
            return True
    return False

def fun_nth_kaprekarnumber(n):
    l = []
    i = 1
    c = 0
    while(c<=n):
        if(kaprekar(i)==True):
            c = c + 1
            l.append(i)
        i = i+1
    return l[n]