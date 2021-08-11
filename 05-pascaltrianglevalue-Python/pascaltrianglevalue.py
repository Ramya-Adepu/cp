# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

def fun_pascaltrianglevalue(row, col):
	l=[1,1]
	cnt=1
	if(col>row+1):
		return 0
	else:
		while(cnt<row):
			m=[]
			m.append(l[0])
			i=0
			n=len(l)
			while(i<n-1):
				m.append(l[i]+l[i+1])
				i+=1
			m.append(l[n-1])
			print(m, cnt)
			l=m
			cnt+=1
		return l[col]

# print(fun_pascaltrianglevalue(7, 9))

    # (1, 1, 1), (3, 5, 0),
    # (3, 1, 3), (5, 2, 10),
    # (6,3,20), (6,2,15),
    # (7, 4, 35), (7, 9, 0)