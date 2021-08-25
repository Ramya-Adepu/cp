# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	l=len(a)
	if(l==0):
		return None
	elif(l%2!=0):
		return a[l//2]
	else:
		mid=l//2
		median=(a[mid]+a[mid-1])/2
		return median


	# ([1, 2, 3, 4, 5], 3),
	# ([1.1, 2.1, 3.1, 4.1, 5.1], 3.1),
	# ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
	# ([1, 2, 3, 4, 5.5, 5.1, 7, 8, 9, 10], 5.3),
	# ([1], 1),
	# ([], None)

print(median([1, 2, 3, 4, 5.5, 5.1, 7, 8, 9, 10]))