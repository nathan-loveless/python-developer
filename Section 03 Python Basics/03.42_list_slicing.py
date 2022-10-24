# List Slicing
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart)
print(amazon_cart[0:2])
print(amazon_cart[0::2])

# Lists are mutable
amazon_cart[0] = 'laptop'

# With list slicing you are creating a new copy of the list, not changing the existing list
print(amazon_cart[0:3])
print(amazon_cart)

new_cart = amazon_cart[0:3]
print(new_cart)

# What happens if you assign new_cart to amazon cart?

new_cart = amazon_cart[:]  # This is copying the list, it does not modify the original because [:] returns a copy
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
