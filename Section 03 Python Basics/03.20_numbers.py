# Fundamental Data Types
# int
# float

# Integers are a number 3, 4, 0
# integers, these in the print statement are whole numbers
print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)

# type() tells the type of the number printed
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
# Notice this is type float
print(type(2 / 4))
print(type(0.00001))
print(type(5.00001))
print(type(0))

# Python converts this intrinsicly into floating point number
print(type(20 + 1.1))

# Python still counts this as a floating point number even though it is 1e1, it keeps the .0 floating point number
print(9.9 + 1.1)
print(type(9.9 + 1.1))

# the ** means power of
print(2 ** 2)

## this (//) returns an integer rounded down
print(2 // 3)
print(type(2 // 3))
print(5 // 4)
print(type(5 // 4))

# Modulo operator, returns the remainder of hte operation
print(5 % 4)
print(6 % 4)
