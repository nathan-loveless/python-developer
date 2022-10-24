# Escape Sequence
# This doesn't work, it thinks the 2nd single quote is the termination of the string and the 3rd is the start
# of a new string
# weather = 'It's sunny'

# Instead we can do this
weather = "It's sunny"

# But what if we wanted to add double quotes as part of the string?
# This doesn't work
# weather = "it's "kind of" sunny"

# We can add slashes
weather = "It\'s \"kind of\" sunny"
print(weather)

# If you need a backslash in your string you can add a second backslash, anything after the 1st backslash will be
# considered a string
weather = "It\\s \"kind of\" sunny"
print(weather)

# Other Escape sequences
# \t - adds a tab
weather = "\t It's \"kind of\" sunny"
print(weather)

# \n - adds a newline
weather = "It's \n \"kind of\" sunny"
print(weather)

# There are many other escape sequences
