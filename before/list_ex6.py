def sublist(n):
    count = 0
    for i in n:
        if type(i) == list:
            count += 1
    return count


mixed = [1, 2, 3, [5, 7, 6], 4, 8, [1, 5, 9]]
print("Number of sublists in list:-", sublist(mixed))
