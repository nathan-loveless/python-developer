# Scope rules
# What variables do I have access to?

# Rules
# 1 start with local scope
# 2 Parent local?
# 3 Global (file)
# 4 Built-In Python functions

a = 1


def confusion():
    a = 5
    return a


print(a)
print(confusion())
