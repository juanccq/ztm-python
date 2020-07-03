from PIL import Image, ImageFilter

img = Image.open( './images/goku.png' )

# print the object
print( img )

# print some attributes
print( img.format )
print( img.size )
print( img.mode )

# print all method Image has
print( dir( img ) )

# blur an image and save it
filtered_img = img.filter( ImageFilter.BLUR )
filtered_img.save( "./images/goku_blur.png", "png" );

# set to grayscale
filtered_img = img.convert('L')

# resize image
filtered_img = filtered_img.resize( (50,50) )

#rotate the image
filtered_img = filtered_img.rotate(90)
filtered_img.save( "./images/goku_gray.png", "png" );
# open the image with the default image viewer of OS
filtered_img.show();

# resize an image keeping the aspect ratio
img = Image.open( './images/vegeta.png' );
img.thumbnail( ( 200,200 ) );
img.save( './images/thumb_vegeta.png', 'png' );