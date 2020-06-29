import sys
from random import randint

start = int(sys.argv[1])
end = int(sys.argv[2])

randvalue = randint(start, end)

while True:
	guess = input('guess the number: ')

	if int(guess) == randvalue:
		print( f'Yeah the random number is {randvalue}' )
		break