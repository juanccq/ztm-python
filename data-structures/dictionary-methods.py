user = {
	'name':'juan',
	'items': [3,5,3]
}

print(user.get('age',37))


user2 = dict(name='jhohanes')
print(user2)

user3 = user2.copy()
print(user3)

user3.update({'name':'jose'})
print(user3)
user3.update({'lastname':'pepe'})
print(user3)