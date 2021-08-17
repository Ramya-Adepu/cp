# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# Your code goes here
	colsum=[]
	rowsum=[]
	dlsum=0
	drsum=0
	for i in range(len(a)):
		row=0
		col=0
		for j in range(len(a[0])):
			if(i==j):
				dlsum+=a[i][j]
				col+=a[j][i]
				row+=a[i][j]
			if(len(a)-1-i==len(a[0])-1-j):
				drsum+=a[len(a)-1-i][len(a[0])-1-j]
				# col+=a[j][i]
				# row+=a[i][j]
			else:
				col+=a[j][i]
				row+=a[i][j]
		colsum.append(col)
		rowsum.append(row)
	if(dlsum!=drsum):
		return False
	elif(len(set(rowsum))!=1):
		return False
	elif(len(set(colsum))!=1):
		return False
	else:
		return True
ismostlymagicsquare([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 1]])

	# ([[2, 7, 6], [9, 5, 1], [4, 3, 8]], True),
	# ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], False),
	# ([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 1]], True)