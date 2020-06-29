import re

string = 'this is a common piece of textto be searched, please use this carefully'

result = re.search( 'piece', string )

print( result.span() )
print( result.start() )
print( result.group() )
print( result.end() )


print( 'with patterns:' )

pattern = re.compile('this')
result = pattern.search( string )
print(result.group())

resall = pattern.findall(string)
print(resall)

resfull = pattern.fullmatch(string)
print(resfull)

resmatch = pattern.match(string)
print(resmatch.group())