# map(), filter(), zip(), and reduce()

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, my_list)))

# map does not change the original list
print(my_list)
