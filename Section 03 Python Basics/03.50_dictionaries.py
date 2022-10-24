# Dictionaries also called hash table or map. This is another data structure.  A dictionary may not be in contiguous
# memory, so you can't access it by index. A dictionary is an unordered key, value pair
dictionary = {
    'a': 1,
    'b': 2,
    'x': 3
}

# you can access by key
print(dictionary['b'])

# You can mix data in a dictionary
dictionary2 = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

print(dictionary2['a'])
print(dictionary2['a'][1])

# You can do this with lists too
my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'hello',
        'x': True
    }
]

print(my_list[0]['a'])
print(my_list[0]['a'][2])

# When should you use a list vs. dictionary.
# A dictionary has no order
# A list has order
# Dictionary holds more data and has a key
