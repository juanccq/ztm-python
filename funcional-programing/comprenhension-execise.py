# return duplicates item
some_list = [ 'a', 'b', 'c', 'b', 'd', 'm', 'n', 'n' ]


duplicates = list({ item for item in some_list if some_list.count(item) > 1 })
print( duplicates )