def super_fun(*args, **kwargs):
	total = 0;
	for items in kwargs.values():
		total += items

	return sum(args)+total

print( super_fun(1,2,2,3,4, num1=2, num2=5) )

# Rule for paramters : params, *args, default parameters, **kwargs