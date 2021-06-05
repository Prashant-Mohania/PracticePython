if __name__ == "__main__":
    def nextPallindrome(n):
        '''return next palindrome number if it is not a palindrome number'''
        n = n + 1
        while not isPallindrome(n):
            n = n + 1
        return n

    def isPallindrome(n):
        '''Check palindrome or not and return boolean'''
        return str(n) == str(n)[::-1]
    try:
        user = int(input("How many number you want to give :- "))
        lst = [int(input("Enter number:- ")) for i in range(user)]
        result = [i if i < 10 else nextPallindrome(i) for i in lst]
        print(result)
    except:
        print("Please enter integer number")
