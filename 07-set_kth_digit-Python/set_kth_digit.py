# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	flag=False
	if(n<0):
		n=abs(n)
		flag=True
	cnt=0
	s=0
	i=0
	# print("r", "n", "s", "cnt", "i")
	while(n>0):
		r=n%10
		n=n//10
		if(cnt==k):
			# print(d*(10**i))
			s+=d*(10**i)
		else:
			s+=r*(10**i)
		# print(r, n, s, cnt, i)
		i+=1
		cnt+=1
	while(cnt<=k):
		if(cnt==k):
			s+=d*(10**i)
		i+=1
		cnt+=1
	if(flag):
		return -1*s
	return (s)

print(fun_set_kth_digit(468, 3, 1))