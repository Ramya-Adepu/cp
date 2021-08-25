# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	l1=len(s1)
	l2=len(s2)
	i=0
	j=0
	k=0
	s=""
	while(i<l1 and j<l2):
		if(k%2==0):
			s+=s1[i]
			i+=1
			k+=1
		else:
			s+=s2[j]
			j+=1
			k+=1
	while(i<l1):
		s+=s1[i]
		i+=1
		k+=1
	while(j<l2):
		s+=s2[j]
		j+=1
		k+=1
	return s
	