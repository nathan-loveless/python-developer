# Docstrings

def test(a):
    """
    Info: this function tests and prints param a
    """
    print(a)


test('!!!!')
# This will also tell you the docstring
help(test)

# You can do it this way
print(test.__doc__)
