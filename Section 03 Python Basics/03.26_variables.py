# Variables store information that can be used in our programs.  They are stored in memory
# Python is loosely typed, it will try to implicitly store the correct data type

# Rules of variable names
# snake_case all lowercase with underscores
# Must start with a lowercase or underscore
# Can use letters, numbers, and underscores, but cannot start a variable with a number
# Variables are case-sensitive
# Don't overwrite keywords
user_iq = 190
print(user_iq)

# you can use these to.  Keep in mind an _ signifies a private variable that we will go over later on
# _user_iq
# us4er_iq3
# user_IQ is different from user_iq


# You do not want to overwrite keywords
# print is a keyword it will give you an error
# You can't overwrite built-in types like int or float

user_age = user_iq / 4
print(user_age)

# Classes have a different convention that we will use later on

# Constants are things that never change in a program
# Constants are all in caps
PI = 3.14

# Double underscores are called dunder, we will learn about these later on
# These are supposed to be left alone and do not make variables with double underscores

# There is a way to use a,b,c = 1,2,3.  This is a quick way to assign variables
a, b, c = 1, 2, 3

print(a)
print(b)
print(c)
