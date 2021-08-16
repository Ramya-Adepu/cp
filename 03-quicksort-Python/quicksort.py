"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def partition(arr, low, high):
	i=(low-1)
	pivot=arr[high]
	for j in range(low, high):
		if(arr[j]<=pivot):
			i=i+1
			arr[i], arr[j]=arr[j], arr[i]
	arr[i+1], arr[high]=arr[high], arr[i+1]
	return i+1

def quick(arr, low, high):
	if(len(arr)==1):
		return arr
	if low<high:
		pi=partition(arr, low, high)
		quick(arr, low, pi-1)
		quick(arr, pi+1, high)

def quicksort(array):
	# Your code goes here
	n=len(array)
	quick(array, 0, n-1)
	print(array)
	return array


quicksort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14])