import random
try:
    # check user input is equal to target or not
    def guessNumber(target):
        '''check input number is equal to given or not'''
        check = True
        times = 1
        while check:
                player = int(input("Guess number:- "))
                if player < target:
                    print("Wrong\nYou guess smaller number")
                    times += 1
                elif player > target:
                    print("Wrong\nYou guess larger number")
                    times += 1
                else:
                    print(f"Congratulation\nYou guess the right number in {times} times")
                    check = False
        return times
    # generate random number
    def generateRandomNumber(a, b):
        '''return random number between a and b'''
        return random.randrange(a, b)
except:
        raise TypeError("Please enter only integer number")
if __name__ == "__main__":
    try:
        mn, mx = input("Enter minimum and maximum number:- ").split(' ')
        target = generateRandomNumber(int(mn), int(mx))
        print("Player 1 :-")
        p1 = guessNumber(target)
        print("Player 2 :-")
        target = generateRandomNumber(int(mn), int(mx))
        p2 = guessNumber(target)
        if p1 < p2:
            print("Player 1 win the game")
        elif p1 == p2:
            print("Match drawn")
        else:
            print("Player 2 win the game")

    except:
        raise TypeError("Please enter only integer number")