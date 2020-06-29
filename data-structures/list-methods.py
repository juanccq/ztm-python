basket = [1,2,3,4,5]

# methods on python doesnt return the new arrasy

#adding
basket.append(11)
print(basket)

basket.insert(3,44)
print(basket)

basket.extend([300,302])
print(basket)

print('removing')

# removing
basket.pop()
print(basket)

basket.pop(1) # return the value removed
print(basket)

basket.remove(44)
print(basket)

basket.clear()
print(basket)