# Sets
# Unordered collections of unique objects
# If you add another 5, it will remove it, each item has to be unique
my_set = {1, 2, 3, 4, 5, 5}
print(my_set)

# You can't access set items with subscripts
# print(my_set[0])
print(1 in my_set)
print(len(my_set))

# You can convert it into a list
print(list(my_set))

new_set = my_set.copy()
print(new_set)
