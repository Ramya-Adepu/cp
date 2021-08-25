# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2
def prime(i):
	if(i%2==0):
		return False
	else:
		n=i//2
		j=3
		while (j<n+1):
			if(i%j==0):
				return False
			j+=2
		return True

def palindrome(n):
	r=str(n)
	l=r[::-1]
	# print(r, l)
	if(int(r)==int(l)):
		# print(r, l)
		return True
	else:
		return False

def fun_nth_palindromic_prime(n):
	if(n==0):
		return 2
	else:
		i=3
		cnt=0
		while cnt<n:
			if(prime(i) and palindrome(i)):
				cnt+=1
				if(cnt==n):
					return i
			i+=2
		# return i

# (0,2),(1,3),(10,313),(15,757),(20,10301),(25,12421)
print(fun_nth_palindromic_prime(25))
# 0  1  2  3  4   5    6    7    8    9    10   11   12   13   14   15   16   17  18     19    20    25
# 2  3  5  7  11  101  151  181  191  313  353  373  383  727  757  797  919  929  10301 10501 10601 12821