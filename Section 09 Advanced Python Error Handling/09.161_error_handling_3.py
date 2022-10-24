# Error handling 3

while True:
    try:
        age = int(input('what is your age?: '))
        10 / age
        raise ValueError('hey cut it out')
    except ValueError:
        print('please enter a number')
    except ValueError:  # The first except block is the only one that will run
        print('!!!!')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('Thank you!')
        break
    finally:
        print('ok, I am finally done')
