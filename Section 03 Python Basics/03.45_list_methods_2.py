# List Methods 2
basket = ['a', 'b', 'c', 'd', 'e', 'd']

# Index asks for what you want to find, and it will throw an error if not found
print(basket.index('d'))

# you can give an option argument on where to start running and finish
print(basket.index('d', 0, 4))

# What if you don't want an error to be thrown if it is not in the list?
print('d' in basket)
print('i' in 'hi my name is Nathan')

# Count, counts how many times something is found in a list
print(basket.count('d'))
