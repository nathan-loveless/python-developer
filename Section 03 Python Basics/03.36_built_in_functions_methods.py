# Python has built-in functions that we have been using already
# This prints the length of our string
print(len('hellloooo'))

greet = 'hellloooo'
print(greet[:])
print(greet[0:len(greet)])

# Built-in Methods
# Fuctions are print()
# Methods are similar to functions but owned by something. We have string methods in Python
# .format()
quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.lower())

# returns the index of what is found, if found. -1 if not found
print(quote.find('be'))
quote2 = quote.replace('be', 'me')

# replace does not overwrite the string, it returns a new string, remember strings are immutable
print(quote)
print(quote2)
