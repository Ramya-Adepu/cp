# Pool balls are arranged in balls where the first row contains 1 pool ball and each row contains 1
# more pool ball than the previous row. 
# numberOfPoolBallRows(balls) that takes a non-negative int number of pool balls, and returns the 
# smallest int number of balls required for the given number of pool balls. Thus, numberOfPoolBallRows(6) 
# returns 3. Note that if any balls must be in a row, then you count that row, and so 
# numberOfPoolBallRows(7) returns 4 (since the 4th row must have a single ball in it).

import math
def fun_numberofpoolballrows(balls):
	n=balls*2
	c=round(math.sqrt(n))
	return c

print(fun_numberofpoolballrows(4999950000))
# (1, 1),(3, 2),(6, 3),(7, 4),(10, 4),(15, 5),(21, 6),(28, 7),(36, 8),(45, 9),(55, 10),(56, 11),
	# (66, 11),(78, 12),(77, 12),(91, 13),(105, 14),(120, 15),(5050, 100),(500500, 1000),(4999950000, 99999)