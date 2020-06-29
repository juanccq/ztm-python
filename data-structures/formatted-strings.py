# formatted strings
name = 'Johnny'
age = 55

print( 'Hi ' + name + '. You are ' + str(age) + ' years old' )

print( f'Hi {name}. You are {age} years old' )

# python 2 style
print( 'Hi {}. You are {} years old'.format( name, age ) )

print( 'Hi {new_name}. You are {age} years old'.format( new_name='juan', age=37 ) )