# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricexcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards).
# Hint: you may want to use fabricyards, which you just wrote!

# (0,0),(1,1),(35,1),(36,1),(37,2),(38,2),(72,2),(73,3)
import math
def fabricyards(inches):
	# Your code goes here...
	# if(inches==0):
	# 	return 0
	# else:
	c=inches/36
	d=math.ceil(c)
	return d

    # (0,0),(1,35),(35,1),(36,0),(37,35),(38,34),(72,0),(73,35)
def fabricexcess(inches):
	# Your code goes here...
	c=inches/36
	d=math.ceil(c)
	r=((d*36-inches))
	return r

print(fabricexcess(73))