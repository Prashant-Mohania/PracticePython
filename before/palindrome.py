user = input("enter :- ")
def is_palindrome(user):
    return user== user[::-1 ]

print(is_palindrome(user))