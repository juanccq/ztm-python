def sum(num1,num2):
	def another_fun(num1, num2):
		return num1+num2
	return another_fun

total = sum(10,8)
print(total(4,7))