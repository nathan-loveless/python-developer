# Dictionary
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

# If you try a key that does not exist like this, you will get an error
# If you want to check to see if a key exists use .get  It will return none if the key does not exist
# If you want to give a default value but give a default value if the key doesn't exist you can also add it like below
# If the key does exist it will not set the default value, instead it will return the value
print(user.get('age', 55))

# Uncommon way to create a dictionary
user2 = dict(name='JohnJohn')

print(user2)
