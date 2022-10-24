# List Methods
basket = [1, 2, 3, 4, 5]
print(len(basket))

# adding
new_list = basket.append(100)
print(basket)
print(new_list)  # New list is None because append changes the list in-place

# You have to do this
basket.append(100)
new_list = basket
print(new_list)

# Insert
basket.insert(4, 50)
print(basket)

# Extend
basket.extend([100, 101])
print(basket)

# Removing
basket.pop()  # pops off the end
print(basket)

basket.pop(0)  # pops at index 0
print(basket)

# this is the value you want to remove not the index. It will only remove the 1st occurrence of the value to remove
# .remove does not return the value removed.  .pop() does return a value
basket.remove(100)
print(basket)

# Clear removes whatever is in the list, but it does not make it None, it makes it an empty list
basket.clear()
print(basket)
