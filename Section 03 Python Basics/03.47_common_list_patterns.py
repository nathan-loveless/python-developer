# Common List Patterns
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()

# Length
print(len(basket))

# Reverse in list slicing
basket.reverse()
print(basket)

# List slicing created a new list, it does not modify the original list
print(basket[::-1])
print(basket)

# Range[start:stop] a quick way to create a numbered list quickly
print(list(range(101)))

# Join it is a string method but used frequently. It creates a new array. Notice that whatever is in sentence is joined
# with each iterable item
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Jojo'])
print(new_sentence)

# Quick way to do this
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'Jojo'])
print(new_sentence)
