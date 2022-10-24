# Generators
# Allows us to generate a sequence of values over time

# range() is a generator, we have used it before
# generates the numbers 1 at a time, it is not being stored in memory


# Generates an entire list in memory, it takes up space in memory
# list(range(100))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(100)
print(my_list)
