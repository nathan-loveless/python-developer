# Exercises: Error Handling

while True:
    try:
        age = int(input('what is your age?: '))
        10 / age
    except ValueError:
        print('please enter a number')
        continue
    except ValueError:  # The first except block is the only one that will run
        print('!!!!')
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('Thank you!')
        break
    finally:  # No matter what, this will run, it runs whether except runs or any other condition is hit, good for logs
        print('ok, i\'m finally done!')
    print('can you hear me')  # if you break out of loop finally runs but this one won't
