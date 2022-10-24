# Decorators
# Decorators have the @ symbol in front of it. Functions are first class citizens in Python
# They can be passed around like variables or as an argument.  Decorators are only possible because functions
# are first class citizens

# Decorators supercharge our function
@decorator
def hello(func):
    func()


def greet():
    print('still here')


# greet = hello
# del hello  # This just deletes the name reference, however greet is still pointing to the memory location
# print(greet())

a = hello(greet)
print(a)
