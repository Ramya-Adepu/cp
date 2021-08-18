# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
def powerfulno(n):
	n=abs(n)
	while(n%2==0):
		a=0
		while(n%2==0):
			n=(n//2)
			a=a+1
		if(a==1):
			return False
	for i in range(3, n):
		a=0
		while(n%i==0):
			n=n//i
			a=a+1
		if(a==1):	
			return False
	return (n==1)

def nthpowerfulnumber(n):
	# Your code goes here
	x=1
	count=-1
	while (count<=n):
		if(powerfulno(x)):
			count=count+1
		if(count==n):
			return x	
		x=x+1
	return 0

	
	
print(nthpowerfulnumber(53))
	# (53, 1000), 
	# (39, 576), 
	# (29, 343), 
	# (17, 128), 
	# (18, 144), 
	# (19, 169), 
	# (4, 16), 
	# (5, 25), 
	# (6, 27), 
	# (7, 32), 
	# (8, 36), 
	# (9, 49), 
	# (10, 64), 
	# (0, 1)
