# only allow unique elements
my_set = {1,2,3,4,5,5}
my_set.add(100)
my_set.add(3)

print(my_set)

my_list = [1,2,2,3,4,4,5]
print(set(my_list))

# set doesnt support index access my_set[1]

print(2 in my_set)

# convert to list , duplicates arent take into account
print(list(my_set))

new_set = my_set.copy()
my_set.clear()
print(new_set)

# other methods
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print('difference')
print(my_set.difference(your_set))

print('discard')
my_set.discard(5)
print(my_set)

my_set = {1,2,3,4,5}
print('difference update')
my_set.difference_update(your_set)
print(my_set)

my_set = {1,2,3,4,5}
print('intersection')
print(my_set.intersection(your_set))

# abreviate mode of intersection
print(my_set & your_set)

print('isdisjoint')
print(my_set.isdisjoint(your_set))

print('union')
print(my_set.union(your_set))

# abreviate mode of union
print(my_set | your_set)

my_set = {4,5}
your_set = {4,5,6,7,8,9,10}

print('issubset')
print(my_set.issubset(your_set))

print('issupperset')
print(your_set.issuperset(my_set))