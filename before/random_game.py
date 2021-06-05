import random
winning_number = random.randint(1, 100)
guess = 1
user = int(input("guess the number b/w 1 to 100 ;- "))
game_over = False
while not game_over:
    if user == winning_number:
        print(f"you win, and you guessed this number in {guess} times ")
        guess += 1
        game_over = True
    else :
        if user < winning_number:
            print("Too Low")
            guess += 1
            user = int(input("guess again :- "))
        else:
            print("Too High :- ")
            guess += 1
            user = int(input("guess again :- "))