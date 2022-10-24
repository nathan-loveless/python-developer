# Iterables
# It is an object or collection that can be iterated over
# list
# dictionary
# tuple
# set
# string

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for item in user.items():
    key, value = item
    print(key, value)

for key, value in user.items():
    print(key, value)
