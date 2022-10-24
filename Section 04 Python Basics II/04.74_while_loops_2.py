# While Loops 2
# For simple loops or iterating over iterable objects for loops are great
# If you are unsure how long you want to loop use while loops

my_list = [1, 2, 3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# Good for user input, don't forget the break or it will go into an infinite loop
while True:
    response = input('Say Something: ')
    if response == 'bye':
        break;
