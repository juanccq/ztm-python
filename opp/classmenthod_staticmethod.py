class PlayerCharacter:

	@classmethod
	def adding_things( cls, num1, num2 ):
		return num1 + num2

	@staticmethod
	def adding_things2( num1, num2 ):
		return num1 + num2

print( PlayerCharacter.adding_things(2,6) )