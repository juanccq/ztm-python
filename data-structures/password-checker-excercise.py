username = input( 'Type your username: ' )
password = input( 'Now your password: ' )
password_length = len( password )
hidden_password = '*' * password_length

print( f'Hi {username}, your password {hidden_password} is {password_length} letters long' )