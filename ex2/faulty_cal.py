print("-----Code by ImPramo-----")
operator = input("Choose operator (+,-,*,/):- ")
num1 = input("Enter First number:- ")
num2 = input("Enter Second number:- ")
if (operator == "+"):
    if (num1 == "56" and num2 == "9"):
        print("77")
    else:
        print(int(num1)+int(num2))
elif (operator == "-"):
    print(int(num1)-int(num2))
elif (operator == "*"):
    if (num1 == "45" and num2=="3"):
        print("555")
    else:
        print(int(num1)*int(num2))
elif (operator == "/"):
    if (num1 == "56" and num2 == "6"):
        print("4")
    else:
        print(int(num1)/int(num2))
