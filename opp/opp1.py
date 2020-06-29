class PlayerCaracter:

	membership = True

	def __init__(self, name, age):
		self.name = name
		self.age = age

		if ( PlayerCaracter.membership ):
			self.name = 'juan'

	def run(self):
		print( 'run' )

	def shout(self):
		print(f'my name is {self.name}')

player1 = PlayerCaracter( 'juan', 33 )
player2 = PlayerCaracter( 'Karen', 77 )
print( player1 )
print( player2 )

print( player1.membership )
print( player2.membership )

print( player1.shout() )
print( player2.shout() )

# help(player1)