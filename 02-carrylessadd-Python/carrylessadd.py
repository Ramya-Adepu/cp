# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.

import math
def fun_carrylessadd(x, y):
	x1=abs(x)
	x2=abs(y)
	result=0
	multiplier=1
	digitsum=0
	while(x1 or x2):
		digitsum=((x1%10)+(x2%10))
		digitsum=digitsum%10
		result=(digitsum*multiplier)+result
		x1=math.floor(x1/10)
		x2=math.floor(x2/10)
		multiplier=multiplier*10
	return result
	# (1, 2, 3),
	# (785, 376, 51),
	# (99, 1, 90),
	# (33,77,0),
	# (121,0,121)
