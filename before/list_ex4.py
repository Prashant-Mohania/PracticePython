def odd_even(n):
    oddn = []
    evenn = []
    for i in n:
        if i % 2 == 0:
            evenn.append(i)
        else:
            oddn.append(i)
    output = [evenn, oddn]
    return output


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(odd_even(numbers))
