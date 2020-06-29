amazon_cart = [
	'notebooks',
	'sunglases',
	'toys',
	'grapes'
]

amazon_cart[0] = 'laptops'
new_cart = amazon_cart[:]  # this is the way to clone a list to prevent new variable makes changes on the original
new_cart[0] = 'gum'

print(new_cart)
print(amazon_cart)