try:
    n = int(input("Enter number of apples:- "))
    mn = int(input("Enter minimum range:- "))
    mx = int(input("Enter maxmum range:- "))

    for i in range(mn, mx + 1):
        if (n % i == 0):
            print(f"{i} is divisor of {n}")
        else:
            print(f"{i} is not a divisor of {n}")
except:
    print("invallled input")
