# method 1
# def evens(n):
#     for even in range(1, n+1):
#         if even % 2 == 0:
#             yield(even)


# for i in evens(10):
#     print(i, end=", ")


# method 2
def evens(n):
    for even in range(2, n+1, 2):
        yield(even)


for i in evens(10):
    print(i, end=", ")
