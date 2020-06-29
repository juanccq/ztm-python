from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,5,5,6,7]
print( Counter( li ) )

sentence = 'blah blah blah blah on python'
print( Counter( sentence ) )

dictionary = defaultdict( lambda:5, {'a':1, 'b':2} )
print( dictionary['c'] )


dictionary = defaultdict( lambda:'item does not exists', {'a':1, 'b':2} )
print( dictionary['d'] )

# OrderedDict check the order even if the dictionaries have the same data
d = OrderedDict()
d[ 'a' ] = 1
d[ 'b' ] = 2

d2 = OrderedDict()
d2[ 'b' ] = 2
d2[ 'a' ] = 1

print( d == d2 )