# Generators 2
# iterable is anything we are able to loop through __iter__
# iterate
# generators are actually iterable, but not everything that is iterable is a generator

def generator_function(num):
    for i in range(num):
        yield i * 2


g = generator_function(1)
next(g)
next(g)
print(next(g))
print(next(g))
# for item in generator_function(1000):
#     print(item)
