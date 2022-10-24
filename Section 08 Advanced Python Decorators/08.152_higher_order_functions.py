# Higher order functions (HOC)
# It can be a function that accepts another function
# A function that returns another function

def greet(func):
    func()


def greet2():
    def func():
        return 5

    return func
