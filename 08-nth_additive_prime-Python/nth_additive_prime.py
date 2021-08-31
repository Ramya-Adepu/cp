# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2




def sum(n):
	sum = 0
	while(n > 0):
		sum = sum + n % 10
		n = n // 10
	return sum
def prime(n):
	if(n < 2):
		return False
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

def fun_nth_additive_prime(n):
	p = 2
	c = -1
	res = 0
	while(True):
		s = sum(p)
		if(prime(p) and prime(s)):
			c = c + 1
			res = p
		p = p + 1
		if(c >= n):
			break
	return res