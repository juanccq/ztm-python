# Lists, set, dicctionary

my_list = [ char for char in 'hello' ]
print( my_list )

my_list2 = [ num for num in range(0,100) ]
print( my_list2 )

my_list3 = [ num**2 for num in range(0,100) ]
print( my_list3 )

my_list4 = [ num**2 for num in range(0,100) if num % 2 == 0 ]
print( my_list4 )

# for sets
my_list = { char for char in 'hello' }
print( my_list )

my_list2 = { num for num in range(0,100) }
print( my_list2 )

my_list3 = { num**2 for num in range(0,100) }
print( my_list3 )

my_list4 = { num**2 for num in range(0,100) if num % 2 == 0 }
print( my_list4 )

# for dictionary
simple_dic = {
	'a': 1,
	'b': 2
}

my_dict = {k:v**2 for k,v in simple_dic.items() if v % 2 == 0}
print( my_dict )

my_dict2 = { num:num**2 for num in [1,2,4] }
print( my_dict2 )