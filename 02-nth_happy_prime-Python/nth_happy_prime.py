# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def prime(n):
	if n < 2:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

def happy(n):
	while(True):
		if n == 1:
			return True
		elif n == 4:
			return False
		else:
			sum = 0
			while(n > 0):
				sum = sum + (n % 10) ** 2
				n = n // 10
			n = sum
			
def fun_nth_happy_prime(n):
	num = -1
	res = 2
	while(True):
		if (prime(res) and happy(res)):
			num = num + 1
		if num == n:
			break
		res = res + 1
	return res
