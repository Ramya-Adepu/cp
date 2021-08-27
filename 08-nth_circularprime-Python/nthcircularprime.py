# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
def primeno(y):
	if(y<2):
		return False
	if(y==2):
		return True
	if(y%2==0):
		return False
	fact=round(y**(1/2))
	for i in range(3, fact+1, 2):
		if(y%i==0):
			return False
	return True

# def digitCount(x):
# 	count=0
# 	n=abs(x)
# 	if(n==0):
# 		return 1
# 	while(n>0):
# 		n=n//10
# 		count=count+1
# 		if n==0:
# 			break	
# 	return count

def circularprime(x):
	n=str(x)
	l=len(n)
	i=0
	while i<l:
		k=n[i:]+n[:i]
		if(not primeno(int(k))):
			return False
		i+=1
	return True	

def nthcircularprime(n):
	# Your code goes here
	count=0
	i=1
	while True:
		if(primeno(i) and circularprime(i)):
			count=count+1
		if(count==n):	
			return i
		if(i>8):
			i=i+2
		else:
			i=i+1	
	return 0
	

print(nthcircularprime(46))

	# (1, 2), (2, 3), (3, 5), (4, 7), 
	# (5, 13), (6, 17), (7, 31), (8, 37), 
	# (9, 71), (10, 73), (11, 79), (12, 97), 
	# (13, 113), (14, 131), (15, 197), (16, 199), 
	# (17, 311), (18, 337), (19, 373), (20, 719), 
	# (21, 733), (22, 919), (23, 971), (24, 991), 
	# (25, 1193), (26, 1931), (27, 3119), (28, 3779), 
	# (29, 7793), (30, 7937), (31, 9311), (32, 9377), 
	# (33, 11939), (34, 19391), (35, 19937), (36, 37199), 
	# (37, 39119), (38, 71993), (39, 91193), (40, 93719), 
	# (41, 93911), (42, 99371), (43, 193939), (44, 199933), 
	# (45, 319993), (46, 331999), (47, 391939)

	

# def nthCircularPrime(x):
# 	count=0
# 	i=1
# 	while True:
# 		if(circularprime(i)):
# 			count=count+1
# 		if(count==x):	
# 			return i
# 		i=i+1	
# 	return 0
# print(nthCircularPrime(int(input())))