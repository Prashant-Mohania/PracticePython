def cube_finder(n):
    num = {}
    for i in range(1,user+1):
        num[i] = i**3
    return num
user = int(input("enter:- "))
print(cube_finder(user))