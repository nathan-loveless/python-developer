import datetime

# Create a program that guesses your age
birth_year = input('what year were you born? ')

# Solve: how do you make it print your age
current_year = datetime.datetime.now().year
age = current_year - int(birth_year)
print(f'You are {age} years old')
