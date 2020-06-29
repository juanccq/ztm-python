# tuples are inmutable
my_tuple = ('a','b','c','d')
print(my_tuple[2])
print('a' in my_tuple)

user = {
	(1,2) : [1,2,3],  # tuple value can be used as key on a dictionary
	'greet' : 'hello',
	'age': 20
}

print(user[(1,2)])


print('other assignements')
new_tuple = my_tuple[1:3]
print(new_tuple)

a,b,c, *evelse = (1,2,3,4,5)
print(a)
print(b)
print(c)
print(evelse)

print( my_tuple.count('a') )
print( my_tuple.index('d') ) # return the index of 'd' element
print( len(my_tuple) )