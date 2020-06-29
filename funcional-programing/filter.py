def only_odd(item):
	return item % 2 != 0

print( list( filter( only_odd, [4,5,6,7] ) ) )