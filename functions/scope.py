a = 1

def parent():
	def func():
		return a
	return func()

print(parent())
print(a)

# order of scoep
#1 start with local
#2 parent local
#3 global
#4 built in python function


total = 0

def count():
	global total
	total +=1
	return total

count()
count()
print( count() )