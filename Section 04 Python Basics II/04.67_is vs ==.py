# is vs ==
print(True == 1)  # true
print('' == 1)  # false
print([] == 1)  # false
print(10 == 10.0)  # true
print([] == [])  # true

# == checks for equality of value

# is checks for type. is checks the location in memory where the value is stored is the same
print(True is 1)  # true
print('' is 1)  # false
print([] is 1)  # false
print(10 is 10.0)  # true
print([] is [])  # true
