from datetime import date

birth_year = int(input( 'what year where you born?' ))
cur_year = int( date.today().year )
print( 'Your age is ' + str(cur_year-birth_year) )