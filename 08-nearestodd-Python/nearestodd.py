# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.


import math
def fun_nearestodd(n):
	x=math.floor(n)
	if(x%2!=0):
		return x
	else:
		if(x==round(n) and x==math.ceil(n)):
			return x-1
		else:
			mn=n-x-1
			mx=x+1-n
			if(mx>mn):
				return x+1
			else:
				return x-1

