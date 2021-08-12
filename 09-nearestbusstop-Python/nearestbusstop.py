# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	r=street%8
	if(r>4):
		print(street+(8-r))
		return street+8-r
	else:
		print(street-r)
	return street-r

fun_nearestbusstop(4)
    # (12, 8), (8, 8),
    # (13, 16), (0, 0),
    # (5, 8), (16, 16),
    # (4, 0)