import time
from functools import wraps


def calculate_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Executing..... {func.__name__}')
        t1 = time.time()
        returned = func(*args, **kwargs)
        t2 = time.time()
        t = t2-t1
        print(f'This function take {t} sec to run')
        return returned
    return wrapper


@calculate_time
def power(num, *args):
    if len(args) > 0:
        return [i**num for i in args]
    else:
        return "Please enter args"


lst = [i for i in range(1, 1000)]
power(3, *lst)
