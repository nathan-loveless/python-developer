# Dictionary
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

# You can also check to see if 'basket' exists in user, it will return True or False
# You can also check to see if it is in keys or values by using .keys() and .values()
# Another way is to use .items()
print(user.items())

# You can also clear the dictionary
# user.clear()
print(user)

# .copy() allows us to copy a dictionary
user2 = user.copy()
print(user)
print(user2)

# .pop() removes a key and returns the removed item
print(user.pop('age'))
print(user)

# .popitem() removes the last item in the dictionary as of 3.7
print(user.popitem())
print(user)

# .update() updates a key/value pair.  If a key does not exist it will create a new key/value
print(user.update({'age': 55}))
print(user)
