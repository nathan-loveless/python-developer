# Return

def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2

    # return keyword automatically exits the function
    return another_func(num1, num2)


# A function should do 1 thing really well
# Should return something
total = sum(10, 20)
print(total)
