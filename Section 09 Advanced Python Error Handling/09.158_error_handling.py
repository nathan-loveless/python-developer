# Error Handling
while True:
    try:
        age = int(input('what is your age?: '))
        10 / age
    except ValueError:
        print('please enter a number')
    except ValueError:  # The first except block is the only one that will run
        print('!!!!')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('Thank you!')
        break
