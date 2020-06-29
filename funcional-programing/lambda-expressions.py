my_list = [5,4,3]

print( list( map( lambda item: item*item, my_list ) ) )

# list sorting by the second value of a tuple
a = [ (0,2), (4,3), (9,9), (10,-1) ]
a.sort( key=lambda item: item[1] )
print( a )