import sys
from PIL import Image
from os import path, listdir, mkdir

source = sys.argv[1]
dest = sys.argv[2]

if not path.exists( source ):
	print( 'Source path does not exists' )
	exit()

if not path.exists( dest ):
	mkdir( dest )
	print( f'Directory {dest} created.' )


for f in listdir( source ):
	if path.isfile( path.join( source, f ) ):
		# print(path.join( source, f ))
		img = Image.open( path.join( source, f ) )

		if( img.get_format_mimetype() == 'image/jpeg' ):
			newname = path.splitext( path.join( dest, f ) )[0]

			img.save( newname+".png", "png" );
			print( 'Image created at ' + newname+".png" )

