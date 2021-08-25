# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.
# def digitCount(x):
# 	count=0
# 	if(x==0):
# 		return 1
# 	while(x>0):
# 		x=x//10
# 		count=count+1	
# 	return count
# def automorphic(n):
#     if(n==0):
#         return  True
#     elif(n==1):
#         return  True    
#     else:
#         square=(n*n)
#         c=digitCount(n)
#         x=square%(10**c)
#         if(n==x):
#             return True
#         return False 
def nthautomorphicnumbers(n):
	# Your code goes here
	# count=0
	# i=0
	# while True:
	# 	if automorphic(i):
	# 		count += 1
    #     # print (count, i)
	# 		if(n == count):
	# 			return i
	# 		i = i + 1
	c = 1
	letest = 0
	num = 1
	while c != n:
		num1 = num
		sqr = num1 * num1
		flag = 0
		while num1>0:
			if num1%10 != sqr%10:
				flag = -1
				break
			num1 = num1 // 10
			sqr = sqr // 10

		if flag==0:
			c+=1
			letest = num

		num = num + 1
	return letest