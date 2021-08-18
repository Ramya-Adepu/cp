# Write the function fun_threelines_area(d1, d2, d3) 
# that takes length of 3 sides
# find the area of a triangle(return an int) given its side lengths.

import math

def fun_threelines_area(a, b, c):
	s=(a+b+c)/2
	a1=s-a
	b1=s-b
	c1=s-c
	d=int(math.sqrt(s*a1*b1*c1))
	return d
	
