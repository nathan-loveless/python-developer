# Break, continue, pass

my_list = [1, 2, 3]
for item in my_list:
    continue
    print(item)

i = 0
while i < len(my_list):
    i += 1
    continue
    print(my_list[i])

# pass
# well pass just passed to the next line, very rare to see pass, maybe as a placeholder until we know what
# we want in a for loop or while loop, leaving a blank for/while loop will cause an error
