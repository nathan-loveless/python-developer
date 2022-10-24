# Why do we need decorators
# Common real-world example, time function for performance
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()  # This starts the time
        result = fn(*args, **kwargs)
        t2 = time()  # This get the end time
        print(f'took {t2 - t1} s')
        return result

    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()
