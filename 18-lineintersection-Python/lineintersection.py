# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.
	# m1*x-y+b1
	# a1x+b1y+c1
	# m2*x-y+b2
	# a2x+b2y+c2
def lineintersection(m1, b1, m2, b2):
	# your code goes here
	if(m1%m2==0 or m2%m1==0):
		return 
	else:
		x=((-1*b2)-((-1)*b1))//((m1*-1)-(m2*-1))
		return x

print(lineintersection(4, 27, 9, 17))

    # (4, 13, 8, 17, None),
    # (2, 13, 2, 14, None),
    # (8, 13, 4, 17, None),
    # (4, 13, 3, 17, 4),
    # (4, 27, 9, 17, 2),