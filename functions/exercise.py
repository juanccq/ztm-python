def highest_even(li):
#	ma = 0
#	for item in li:
#		if item % 2 == 0 and item > ma:
#			ma = item
#	return ma
# another solution
	evens = []
	for items in li:
		if items % 2 == 0:
			evens.append(items)

	return max(evens)

print( highest_even( [10,2,3,4,8,11] ) )