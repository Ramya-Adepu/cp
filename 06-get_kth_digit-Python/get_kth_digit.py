# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	n=abs(digit)
	i=0
	while(n>0):
		r=n%10
		if(i==k):
			return r
		i+=1
		n=n//10
	if(i<=k):
		return 0
	
print(fun_get_kth_digit(-780, 4))
    # (789,0,9), (789,1,8),
    # (789,2,7), (789,3,0),
    # (-789,0,9), (-780,4,0),
