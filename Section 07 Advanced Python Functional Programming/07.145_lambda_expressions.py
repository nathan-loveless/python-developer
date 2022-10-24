# Lambda Functions
# One time anonymous functions that you don't need more than once
# Useful when using them for functions that you use 1 time
# We don't have to store them anywhere in our files
from functools import reduce

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


# multiply_by2
print(list(map(lambda item: item * 2, my_list)))

# only_odd
print(list(map(lambda item: item % 2 != 0, my_list)))

# accumulator
print(reduce(lambda acc, item: acc + item, my_list))
