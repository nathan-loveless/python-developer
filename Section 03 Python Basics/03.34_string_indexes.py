# The string is stored in contiguous order in memory
selfish = '01234567'

# You can access different parts of a string using its index

# this prints the first character of the string or the 0th index
print(selfish[0])

# this prints the 7th index (the 8th character)
print(selfish[7])

# Bracket operators can be used as an index [7] (single index) or a range [start:stop].
print(selfish[0:2])

# You can also use the step-over with brackets [start:step:step-over]
print(selfish[0:8:2])

# Is this valid? Yes, it is it says start at 1 then stop when at the end
print(selfish[1:])

# You can also do this, it starts at 0 and goes up to the 5th element
print(selfish[:5])

# This will start at the beginning to end stepping over 1 time
print(selfish[::1])

# What happens if you put a -1? It starts at the end of the string and counts back
print(selfish[-1])

# You can do this.  It is a common operation.  It means start:stop but step over from the back, it it like reversing
# the order
print(selfish[::-1])
print(selfish[::-2])
