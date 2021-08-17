# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import math
def fun_find_int_roots(a, b, c):
	det=math.sqrt(b*b-(4*a*c))
	root1=int((-b-det)/(2*a))
	root2=int((-b+det)/(2*a))
	# print(root1, root2)
	return root1, root2
print(fun_find_int_roots(1, 3, 2))
# (1, -5, 6, (2,3)),(1, -6, 8, (2,4)),
# (1, 1, -12, (-4,3)),(1, -6, 5,(1,5)),
# (1, 3, 2,(-2,-1))

