from functools import reduce

my_list = [1,2,4]
print( list( map( lambda item: item*2, my_list ) ) )

print( reduce( lambda acc, item: acc + item, my_list ) )