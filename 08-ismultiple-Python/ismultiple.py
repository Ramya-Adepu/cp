# Write the function isMultiple that takes two int values m and n 
# and returns True if m is a multiple of n and False otherwise. 
# Note that 0 is a multiple of every integer including itself. 
# Also, you should make constructive use of the isFactor function you just wrote above.

def fun_ismultiple(m, n):
	if(m==0 or n==1):
		return True
	elif(n==0 or m<n):
		return False# replace with your solution
	elif(m%n==0):
		return True
	else:
		return False
