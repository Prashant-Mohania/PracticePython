def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Denominator con\'t be 0")

try:
    a = int(input("Enter:-"))
    b = int(input("Enter:-"))
except ValueError:
    print("PLEASE ENTER INTEGER")
except:
    print("UNEXPECTED ERROR")
else:
    print(divide(a, b))
