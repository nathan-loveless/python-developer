# Truthy and Falsy
# In the if statement Python is converting to booleans
is_old = 'hello'
is_licensed = 5

# These are both true when converted
print(bool('hello'))
print(bool(5))

# Falsy values
print(bool(''))
print(bool(0))

if is_old and is_licensed:
    print('You are old enough to , and you have a license')
else:
    print('You are not of age!')
