# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
    n=abs(n)
    count=1
    max_count=0
    a=12
    b=0
    if(n==0):
        return n
    if(n<9):
        return n
    while(n>0):
        r=n%10
        if(r!=a):
            count=1
        n=n//10
        if(a==r):
            count=count+1
        a=r
        if(count>max_count):
            max_count=count
            b=a
        if(max_count==count):
            if(b>a):
                b=a
    return b
    
	# (117773732, 7), 
    # (-677886, 7), 
    # (112233455567, 5), 
    # (44332211, 1), 
    # (4422113355, 1),
    # (12345, 1), 
    # (123330001, 0)