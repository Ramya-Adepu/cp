# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.




def fun_alternatingsum(a):
	i=0
	s=0
	while(i<len(a)):
		if(i%2==0):
			s+=a[i]
		else:
			s-=a[i]
		i+=1
	return s


