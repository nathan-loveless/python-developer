# Dictionary Keys
# A key has to be immutable
# [100]: True is mutable and therefore will not work.  123 and True and '[100]' will work as keys
dictionary = {
    123: [1, 2, 3],
    True: 'hello',
    '[100]': True
}

print(dictionary['[100]'])

dictionary2 = {
    '123': [1, 2, 3],
    '123': 'hello'
}

# It will remove one of the '123' keys.  What really happens is it overwrites a key/value pair
# to make '123' unique in the list
print(dictionary2['123'])
