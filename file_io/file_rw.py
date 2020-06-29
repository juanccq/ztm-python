filecontent = open( 'test.txt' )

print( filecontent.read() )

filecontent.seek(0) # use this cause after read, the cursor its on the end of file
print( filecontent.read() )
filecontent.close()

filecontent = open( 'test.txt' )
print( filecontent.readline() )
print( filecontent.readline() )
print( filecontent.readline() )
filecontent.close()

filecontent = open( 'test.txt' )
print( filecontent.readlines() )
filecontent.close()