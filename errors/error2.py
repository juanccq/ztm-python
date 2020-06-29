def div(num1, num2):
	try:
		num1/num2
	except (TypeError, ZeroDivisionError) as err:
		print(f'There is an error: {err}')


div(2,0)