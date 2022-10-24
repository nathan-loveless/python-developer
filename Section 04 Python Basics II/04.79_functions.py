# Functions
# DRY - Do Not Repeat Yourself, this makes functions very

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def say_hello():
    print('hello')


def show_tree():
    for image in picture:
        for pixel in image:
            if (pixel):
                print('*', end="")
            else:
                print(' ', end="")
        print('')


say_hello()
show_tree()
show_tree()
show_tree()
