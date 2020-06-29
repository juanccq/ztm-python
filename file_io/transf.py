from translate import Translator

translator = Translator( to_lang='zh' )


try:
	with open( 'test.txt' ) as my_file:
		lines = my_file.readlines()

	for line in lines:
		print( line )
		translation = translator.translate( line );
		print( translation )

except FileNotFoundError as err:
	print( 'Source file does not exists' )
	raise err
except IOError as err:
	print( 'Error on I/O file' )
	raise err