# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math
def iskaprekar(n):
    if n == 1 :
        return True
    n2 = n * n
    # print(n2)
    digitcnt=len(str(n2))
    # print(digitcnt)
    i=0
    n2=str(n2)
    while i<digitcnt:
        s1=n2[:i]
        s2=n2[i:]
        # print(len(s1), len(s2))
        if(len(s1)>0 and len(s2)>0):
            a=int(n2[:i])+int(n2[i:])
            # print(n2, a, int(n2[:i]), int(n2[i:]))
            if(a==n and a!=100):
                # print(n2[:i]+n2[i:], a, n)
                return True
        i+=1
    return False

def fun_nearestkaprekarnumber(n):
    i=n
    j=n
    while True:
        # print(i, j)
        if(iskaprekar(j)):
            # print("loop entering")
            return j
        elif(iskaprekar(i)):
            return i
        i+=1
        j-=1

# (49,  45), (51,  55), (50,   45),
# (102, 99), (765, 703),(3861, 4879)
print(fun_nearestkaprekarnumber(100))