# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


def oldest(*args):
    oldest_cat = args[0]

    for cat in args:
        if oldest_cat.age < cat.age:
            oldest_cat = cat

    return oldest_cat


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Cookie', 1)
cat2 = Cat('Mercury', 5)
cat3 = Cat('Lulu', 2)

# 2 Create a function that finds the oldest cat
oldest_cat = oldest(cat1, cat2, cat3)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat.age} years old')
