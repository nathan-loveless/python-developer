# List Methods 3
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

# Sort, sorts the list in place, so you need to use sort before printing it
basket.sort()
print(basket)

#  Sorted returns sorted list, it does not do it in-place.  It will keep the original copy of the list unmodified
print(sorted(basket))

# Copy
new_basket = basket.copy()
print(new_basket)

# Reverse reverses the list in-place
basket.reverse()
print(basket)
