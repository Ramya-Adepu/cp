# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	mx=999999
	s=1
	d=dict()
	if(n==0):
		return 0
	else:
		while(n>0):
			r=n%10
			if r in d:
				d[r]+=1
				if(d[r]>s):
					s=d[r]
					mx=r
				elif(d[r]==s and mx>r):
					mx=r
			else:
				d[r]=1
				if(d[r]>=s):
					s=d[r]
					if(mx>r):
						mx=r
			n=n//10
		return mx

# print(mostfrequentdigit(24))
print(mostfrequentdigit(0))
# print(mostfrequentdigit(26011))
# print(mostfrequentdigit(14))
# print(mostfrequentdigit(2))
# print(mostfrequentdigit(5))
# print(mostfrequentdigit(5231123123123))
# print(mostfrequentdigit(5312312355565))
# print(mostfrequentdigit(1102300))