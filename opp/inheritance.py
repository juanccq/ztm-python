class User:

	def __init__(self, email):
		self.email = email

	def sign_in(self):
		print( 'logged in' )


	def attack(self):
		print('do nothing')


class Wizard(User):
	def __init__(self, name, power, email):
		super().__init__(email)
		self._name = name
		self._power = power

	def attack(self):
		# call the parent method
		User.attack(self)

		print( f'attacking with power of {self._power}' )

class Archer(User):
	pass


# archer1 = Archer()
# archer1.attack()

wizard1 = Wizard('Merlin', 22, 'merlin@mail.com')
#wizard1.attack()
print( wizard1.email )