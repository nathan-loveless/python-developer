# Decorators 2
# A decorator is a function that wraps another function

def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')

    return wrap_func


@my_decorator
def hello():
    print('hello')


@my_decorator
def bye():
    print('See you later')


bye()

hello()

# How it works
hello2 = my_decorator(hello)
hello2()
