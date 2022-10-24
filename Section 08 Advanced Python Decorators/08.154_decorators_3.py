# Decorators 3
# It is called a decorator because it is called a decorator pattern
# A decorator is a function that wraps another function

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')

    return wrap_func


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


hello('hello')

# How it works
# hello2 = my_decorator(hello)
# hello2()
