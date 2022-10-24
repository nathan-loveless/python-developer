# Useful Modules
# From Python built-in modules

from collections import Counter, defaultdict, OrderedDict

# Counter - creates a dictionary that keeps track of the number of times an item occurs
li = [1, 2, 3, 4, 5, 6, 7, 7]
print(Counter(li))

sentence = 'blah blah blah thinking about python'
print(Counter(sentence))

# defaultdic - allows you to get a default value if something doesn't exist on the list that you try to access
# added a lambda: None, if nothing exists
dictionary = defaultdict(lambda: None, {'a': 1, 'b': 2})
print(dictionary['c'])

# OrderedDict
# Retains the order you insert into a dictionary.  If you compare they will be false

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()

d2['a'] = 2
d2['a'] = 1

print(d2 == d)
