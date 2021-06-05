def square(n):
    sq = []
    for i in n:
        sq.append(i**2)
    return sq


a = int(input("Enter starting number:-"))
b = int(input("Enter end number:-"))
num = list(range(a, b+1))
print(square(num))
