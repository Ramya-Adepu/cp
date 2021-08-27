# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	# Your code goes here
	if(n<1):
		return None
	else:
		k=n//3
		i=0
		a=[]
		while i<k+1:
			x=3**i
			if(x<=n):
				a.append(3**i)
			i+=1
		return a

print(recursion_powersof3ton(100))
	# (0, None), (-42, None),
	# (0.99, None), (1, [1]),
	# (3, [1, 3]), (8.9999, [1, 3]),
	# (9, [1, 3, 9]), (9.1111, [1, 3, 9]),
	# (100, [1, 3, 9, 27, 81])