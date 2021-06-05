user_input = input("Enter:-")
if 1940 <= int(user_input) <= 2020 and len(user_input) == 4:
    age = 2020 - int(user_input)
    print("You turn 100 years in", int(user_input) + 100)
elif len(user_input) < 3 and int(user_input) >= 0:
    age = int(user_input)
    print("You turn 100 years in", (2020 - int(user_input)) + 100)

elif int(user_input) < 1940 and len(user_input) == 4:
    print("You are the oldest person the earth")
    exit()
elif int(user_input) > 2020:
    print("You are not yet born")
    exit()

choice = input("You want to your age in particular year (Yes:- y, No:- n):-")
if choice == 'y':
    userYear = input("Enter year:- ")
    if len(user_input) == 4:
        if int(userYear) > int(user_input) and int(userYear) > int(user_input):
            print(
                f"Your age in {int(userYear)} is {(int(userYear) - 2020) + age}")
        else:
            print("????     invalid input      ????")
    elif len(user_input) == 2:
        if int(userYear) > (2020 - age):
            print(
                f"Your age in {int(userYear)} is {(int(userYear) - 2020) + age}")
        else:
            print("????     invalid input      ????")
print("\nThanks for using it")
