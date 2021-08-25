# matrixAdd(L, M)[10 pts]
# Background: we can think of a 2d list in Python as a matrix in math. To add two matrices, L and M, they must have 
# the same dimensions. 
# Then, we loop over each row and col, and the result[row][col] is just the sum of L[row][col] and M[row][col]. For example:
# L = [ [1,  2,  3],
#       [4,  5,  6] ]
# M = [ [21, 22, 23],
#       [24, 25, 26]]
# N = [ [1+21, 2+22, 3+23],
#       [4+24, 5+25, 6+26]]
# assert(matrixAdd(L, M) == N)
# With this in mind, write the function matrixAdd(L, M) that takes two rectangular 2d lists (that we will consider 
# to be matrices) that you 
# may assume only contain numbers, and returns a new 2d list that is the result of adding the two matrices. Return 
# None if the two matrices 
# cannot be added because they are of different dimensions.
def checkMatrix(x):
	row=len(x)
	col=len(x[0])
	for i in range(row):
		if(len(x[i])!=col):
			return False
	return True

def matrixadd(L, M):
	# Your code goes here
	r1=len(L)
	c1=len(L[0])
	r2=len(M)
	c2=len(M[0])
	if(checkMatrix(L) and checkMatrix(M) and r1==r2 and c1==c2):
		# res=[[0]*c1]*r1
		# print(res)
		res=[]
		for i in range(r1):
			r=[]
			for j in range(c1):
				r.append(L[i][j]+M[i][j])
			res.append(r)
		print(res)
		return res
	else:
		return None

	
matrixadd([[1,  2,  3],[4,  5,  6]], [[21, 22, 23], [24, 25]])
	# ([[1,  2,  3],[4,  5,  6]], [[21, 22, 23], [24, 25, 26]], [[22, 24, 26],[28, 30, 32]]),
	# ([[1,  2,  3],[4,  5,  6], [7, 8, 9]], [[1,  2,  3],[4,  5,  6], [7, 8, 9]], [[2, 4, 6],[8, 10, 12], [14, 16, 18]]),
	# ([[1,  2,  3],[4,  5,  6]], [[21, 22, 23], [24, 25]], None),
	# ([[1]], [[10]], [[11]]),
	# ([[1, 2]], [[10]], None),