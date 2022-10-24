# Formatted Strings
# up until now we have just did simple strings, we don't want to hardcode every single users name
# We can make is dynamic

# If you pretend we are logging into Amazon.com and our name is retrieved from a database
# We want to greet this person below.
name = 'Johnny'
age = 55

print('Hi ' + name + '. You are ' + str(age) + ' years old')

# We can do this better by adding an f in front of the string so it knows it is formatted and we can
# remove all the + and extra quotes.  This is a feature of Python3.
print(f'Hi {name}. You are {age} years old')

# In Python2 it worked like this
print('Hi {}. You are {} years old'.format('Johnny', '55'))

# We can also use variables in Python2
print('Hi {}. You are {} years old'.format(name, age))

# We can change the order as well
print('Hi {0}. You are {1} years old'.format(name, age))

# You can also create your own variables, but you must name them in the string
print('Hi {new_name}. You are {age} years old'.format(new_name='Sally', age=100))
