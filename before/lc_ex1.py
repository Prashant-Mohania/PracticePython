# by List comprehension
def reverse_func(l):
    return [name[::-1] for name in l]

print(reverse_func(['abc', 'pqr', 'xyz']))


# by normal method
def reverse(n):
    for name in n:
        new_list = []
        for name in n:
            new_list.append(name[::-1])
    return new_list

print(reverse(['abc', 'pqr', 'xyz']))
