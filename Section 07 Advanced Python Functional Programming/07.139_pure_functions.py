# Pure Functions
# Rules for pure functions
# 1. Given the same input it should produce the same output
# 2. The function cannot have any side effects, meaning does it affect anything outside the function?

# Pure function produce less buggy code, easier to understand and don't have other parts of your code touching or using
# each other.  Pure functions are more of a guideline rather than an absolute, you can use all pure functions in a
# program.

# new_list = [] This would be a side effect, it is outside the function


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list
    # return print(new_list)  This would be a side effect, it uses the print that prints to a monitor that is outside
    #                         the function


# new_list = '' If you keep the list outside the function, it could be modified and the function would not be a pure
# function
print(multiply_by2([1, 2, 3]))
