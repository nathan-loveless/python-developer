from random import randint

# generate a number 1 - 10
answer = randint(1, 10)

# get input from user?


# check that input is a number 1 - 10
while True:
    try:
        guess = int(input('Guess a number 1 - 10: '))
        if 0 < guess < 11:
            # check if number is the right guess, otherwise ask again
            if guess == answer:
                print('You are correct!')
                break
        else:
            print('Please use 1 - 10')
    except ValueError:
        print('Please enter a number')
        continue
