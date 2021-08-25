# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)
# def primeno(y):
# 	if(y<2):
# 		return False
# 	if(y==2):
# 		return True
# 	if(y%2==0):
# 		return False
# 	fact=round(y**(1/2))
# 	for i in range(3, fact+1, 2):
# 		if(y%i==0):
# 			return False
# 	return True

# def squaresum(n): 
# 	sum = 0
# 	c=0 
# 	while(n): 
# 		sum=sum+(n%10)*(n%10)
# 		n=n//10
# 	return sum

# def happynumber(n):
# 	a=n
# 	b=n
# 	while True:
# 		a=squaresum(a)
# 		b=squaresum(squaresum(b))
# 		if(a!=b):
# 			continue
# 		else:
# 			break
# 	return (a==1)

# def nth_happy_number(n):
# 	count=4
# 	i=13
# 	# if(primeno(i)):
# 	if(n==1):
# 		return 1
# 	# (1,1),(2,7),(3,10),(4,13),(5,19),(6,23),(7,28),(8,31)
# 	elif(n==2):
# 		return 7
# 	elif(n==3):
# 		return 10
# 	else:
# 		while True:
# 			if (primeno(i) == True and happynumber(i)):
# 				count+=1
# 			if(n==count):
# 				return i
# 			i=i+1
# 		return 0
def nth_happy_number(n):
    if n==1:
        return 1
    if n==2:
        return 7
 
    a=2;b=8
    while a<=n:
        if ishappy(b):
            a+=1
        if a==n:
            return b
        b+=1
 
def ishappy(m):
    while(m>=10):
        m=squarenum(m)
        if(m==1):
            return True
    return False
 
def squarenum(b):
    sum=0
    while(b>0):
        rem=b%10
        sum+=(rem*rem)
        b//=10
    return sum