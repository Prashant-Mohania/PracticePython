def power(num, *args):
    if len(args) > 0:
        return [i**num for i in args]
    else:
        return "Please enter args"


print(power(3, 1, 2, 3, 4, 5))
