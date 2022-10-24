# Exercise: Password Checker
username = input('Please type your username: ')
password = input('Please type your password: ')
password_length = len(password)
hidden_password = '*' * password_length

print(f'username: {username}, your password: {hidden_password} is {password_length} letters long')
