class User:

#	def __init__(self, email):
#		self.email = email

	def sign_in(self):
		print( 'logged in' )


	def attack(self):
		print('do nothing')


class Wizard(User):
	def __init__(self, name, power,email):
#		User.__init__(email)
		self._name = name
		self._power = power

	def attack(self):
		# call the parent method
		User.attack(self)
		print( f'attacking with power of {self._power}' )


class Archer(User):
	def __init__(self, name, arrows):
		self._name = name
		self._arrows = arrows

	def check_arrows(self):
		print(f'{self._arrows} remaining')

	def run(self):
		print('ran really fast')

class HybridBorg( Wizard, Archer ):
	def __init__(self, name, power, arrows, email):
		Archer.__init__(self, name, arrows)
		Wizard.__init__(self, name, power, email)
		



# archer1 = Archer()
# archer1.attack()

hb1 = HybridBorg( 'borgie', 50, 75, 'borg@mail.com' )
hb1.attack();
hb1.check_arrows();
hb1.run();
hb1.sign_in();