# Scope
# What variables do I have access to?
# This is global scope (within a file)

if True:
    # You only create a new scope when you define a function, x is still in the global scope
    x = 10


def some_func():
    # total is local to the functional scope
    total = 100


print(x)
