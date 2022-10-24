# Sets

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# .difference() shows the difference between 2 sets without modification
# print(my_set.difference(your_set))

# .discard() discards an item you pass it
# print(my_set.discard(5))
# print(my_set)

# .difference_update() Remove all elements of another set from this set.
# print(my_set.difference_update(your_set))
# print(my_set)

# .intersection() Return the intersection of two sets as a new set.
# print(my_set.intersection(your_set))

# shorthand
# print(my_set & your_set)

# .isdisjoint()  True if two sets have a null intersection.
# print(my_set.isdisjoint(your_set))

# .union() Return the union of sets as a new set.
# print(my_set.union(your_set))

# shorthand
# print(my_set | your_set)

# .issubset() Report whether another set contains this set.
# print(my_set.issubset(your_set))

# .issuperset() Report whether this set contains another set.
print(my_set.issuperset(your_set))
