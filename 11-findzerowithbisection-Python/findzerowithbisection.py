# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.
def funct(x):
	return x*x

def bisection(a, b):
	if (funct(a) * funct(b) >= 0):
        # print("You have not assumed right a and b\n")
		return
	c = a
	while ((b-a) >= 0.01):
		c = (a+b)/2
		if (funct(c) == 0.0):
			break
		if (funct(c)*funct(a) < 0):
			b = c
		else:
			a = c
	return c

def findzerowithbisection(x, epsilon):
	# epsilon and step are initialized
	# don't change these values
	# epsilon
	# your code starts here

	return bisection(1, x)

print(findzerowithbisection(49, 0.01))