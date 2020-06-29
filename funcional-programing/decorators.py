from time import time

def my_decorator(func):
	def wrap_func(*args, **kwargs):
		print('********')
		func(*args, **kwargs)
		print('--------')

	return wrap_func

def performance(fn):
	def wrapper( *args, **kwargs ):
		t1 = time()
		result = fn( *args, **kwargs )
		t2 = time()

		print( f'took {t2-t1} s' )
		return result
	return wrapper

@my_decorator
def hello(name):
	print(f'heloo {name}')


hello('juan')


@performance
def long_time():
	for i in range(1000000):
		i*5

long_time()