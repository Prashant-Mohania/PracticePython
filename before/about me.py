print("Hi!!! I\'m Prashant")
user =input("what is your name:-")
print(f"hey!!! {user}, Nice to meet you.\nplease help me to choose me a pet animal")
dog=(" o____\n   ||||")
sheep= ("o-###-\n  | |")
please ={1:dog,2:sheep}
for key,value in please.items():
    print(f"{key}:{value}")
help=int(input("please help:-"))
if help==1:
    print(f"thanks for helping me to choose dog \n {dog}")
elif help==2:
    print(f"thanks for helping me to choose sheep\n {sheep}")
else:
    print("Invalid option")
born = int(input("enter your DOB?\n"))
age=(2025 - born)
print(f"In 2025 you\'ll be {age} years")
dogs_age = (age *7)
print(f"According to dogs age, you are {dogs_age}")