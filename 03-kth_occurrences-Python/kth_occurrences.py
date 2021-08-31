# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	d = {}
	for i in s.lower():
		if i not in d:
			d[i]=1
		else:
			d[i] = d[i]+1
	l = sorted(d.values(),reverse=True)
	for key,val in d.items():
		if val == l[n-1]:
			return key
	# return 'a'


