from functools import reduce

def accumulator( acc, item ):
	return acc+item

print( reduce( accumulator, [2,3,4], 0 ) )