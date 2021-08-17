# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	a.sort()
	m=99999
	if(len(a)>1):
		for i in range(1, len(a)):
			if(a[i]-a[i-1]<m):
				m=a[i]-a[i-1]
		return m
	else:
		return -1