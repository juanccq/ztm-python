# this method doesnt require to close the file
with open('test.txt') as my_file:
	print( my_file.readline() )


#with open( 'test.txt', 'r+' ) as my_file:
#	text = my_file.write( 'Hey its me' )  # carefull cause this line overwrite from the beginning of the file


#with open( 'test.txt', 'r+' ) as my_file:
#	text = my_file.write( ':)' )	# carefull cause this line overwrite from the beginning of the file

#with open( 'test.txt', 'w' ) as my_file:
#	text = my_file.write( 'all content was replaced' )	# carefull cause this line overwrite all the content

#with open( 'test.txt', 'a' ) as my_file:
#	text = my_file.write( ' added to the end of file' )


# about modes
# r+ open the file contents and overwrite with the new values
# w replace all the content with the new values
# a add caracters at the end of file