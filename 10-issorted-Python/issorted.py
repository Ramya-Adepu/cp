# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	l=len(a)
	if(l<2):
		return True
	else:
		b=a.copy()
		b.sort()
		print(a, b)
		if(a==b or a==b[::-1]):
			return True
		else:
			return False
		# i=1
		# if(a[1]>a[0]):
		# 	flag=True
		# 	x=0
		# else:
		# 	flag=False
		# 	x=1
		# while(i<l):
		# 	if(a[i]<a[i-1]):
		# 		flag=False
		# 		# return False
		# 	elif(a[i]>a[i-1]):
		# 		flag=True
		# 	i+=1
		# if(x==0 and flag==True):
		# 	return True
		# elif(x==1 and flag==False):
		# 	return True
		# else:
		# 	return False

print(issorted([10, -1, 5.5, 5.5, 5.5, 4, 3, 2, 1]))
	# ([1, 2, 3, 4, 5], True),
	# ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True),]
	# ([1], True),
	# ([1, 1], True),
	# ([], True),
	# ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], True),
	# ([10, 9, 8, 7, 6, 5, 4, 3, 2, 10], False),
	# ([1, 2, 3, 4, 5.5, 5.1, 7, 8, 9, 10], False),
	# ([1, 2, 3, 4, 5.5, 5.5, 5.5, 5.5, -1, 10], False),
	# ([10, -1, 5.5, 5.5, 5.5, 4, 3, 2, 1], False),
	# ([-1, 0, -1.1], False)