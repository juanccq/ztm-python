bastek = ['a','b','c','d','e','a','d']

print(bastek.index('c'))


print( 'd' in bastek )

print( bastek.count('a') )


# part 3
bastek.sort();
print(bastek)

basket = bastek.copy()

basket.reverse()
print(basket)

# reverse bi slicing
print(basket[::-1])


#generate
list1 = list(range(2,100))
print(list1)

sentence = ' '
new_str = sentence.join(basket)

print(new_str)

# list unpacking
print('list unpacking')
a,b,c = [1,5,3]
print(a)
print(b)
print(c)


a,b,c, *other = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)

a,b,c, *other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)