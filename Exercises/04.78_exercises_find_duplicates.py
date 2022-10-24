# Exercise: Check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
found_list = []

for chr in some_list:
    try:
        if some_list.count(chr) > 1:
            found_list.index(chr)
    except ValueError:
        found_list.append(chr)

print(found_list)
