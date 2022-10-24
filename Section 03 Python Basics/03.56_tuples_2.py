# Tuple
# You can split tuples
my_tuple = (1, 2, 3, 4, 5, 5)
new_tuple = my_tuple[1:4]
print(new_tuple)

x = my_tuple[0]
y = my_tuple[1]

print(x)
print(y)

x, y, z, *other = (1, 2, 3, 4, 5)
print(z)
print(other)

print(my_tuple.count(5))

print(my_tuple.index(1))
print(len(my_tuple))
