selfish = '01234567'
# selfish[start:stop:stepover] is called slicing
print(selfish)

# Immutibility is important.  It means they cannot be changed.


# If you were to change seflish it would give you an error "str object does not support item assignment"
# selfish[0] = '8'
# print(selfish[0])

# In order to change a string, you must reassign the whole variable.
selfish = '8'
print(selfish)
