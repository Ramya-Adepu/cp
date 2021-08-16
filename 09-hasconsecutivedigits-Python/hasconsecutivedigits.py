# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	s=str(abs(n))
	l=len(s)
	i=1
	if(l==1):
		return False
	else: 
		while(i<l):
			if(s[i-1]==s[i]):
				return True
			i+=1
		return False

print(hasconsecutivedigits(-11023))
	# (-24, False),
	# (0, False),
	# (26011, True),
	# (14, False),
	# (2, False),
	# (5, False),
	# (5231123123123, True),
	# (-5231123123123, True),
	# (-11023, True),