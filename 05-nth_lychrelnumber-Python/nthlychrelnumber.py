# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

maxi = 25
def nthlychrelnumbers(n):
	# your code goes here
		# your code goes here
	c = 1
	i = 196
	res = 0
	while(True):
		# print(islychrel(196))
		if (islychrel(i)):
			# print(c)
			# print(n)
			res = i
			if c == n:
				break
			c = c + 1
		i = i+1
	return res

def islychrel(num):
	for i in range(maxi):
		num = num+reverse(num)
		if(ispalindrome(num)):
			return False
	return True
def ispalindrome(num):
	return num == reverse(num)
def reverse(num):
	rev = 0
	while(num>0):
		r = num%10
		rev = (rev*10)+r
		num = num//10
	return rev