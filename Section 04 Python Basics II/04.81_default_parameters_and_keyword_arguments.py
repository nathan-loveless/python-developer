# Default Parameters and Keyword Arguments

# Positional arguments matters because it must be in the order the parameters are declared

# Default Parameters
def say_hello(name='Darth Vader', emoji='👿'):
    print(f'hello {name} {emoji}')


say_hello('Nathan', '😊')
say_hello('Dan', '😊')
say_hello('Emily', '😊')

# you can use keyword arguments and explicitly tell where they belong
# Not the best practice.  If you use keyword arguments at least put them in order of the parameters.
# This is not default parameters
say_hello(emoji='😊', name='Bibi')

# if you run another function and don't give it parameters, it will use the default parameters
say_hello()

# Same result, it will default to devil emoji
say_hello('Timmy')
