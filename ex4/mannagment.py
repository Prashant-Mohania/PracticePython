def getdate():
    import datetime
    return datetime.datetime.now()


def writefile():
    name = input("Enter (1:- Harry, 2:- Rohan, 3:- Hammad):-\n")
    if name == "1":
        work = input("Enter (1:- Food, 2:- Exercise)\n")
        try:
            if work == "1":
                hf = input("Type here\n")
                with open("harry_food.txt", "a") as wf:
                    wf.write(str([str(getdate())])+": "+hf+"\n")
                    print("Write Successfully")
            elif work == "2":
                he = input("Type here\n")
                with open("harry_exercise.txt", "a") as wf:
                    wf.write(str([str(getdate())])+": "+he+"\n")
                    print("Write Successfully")
        except:
            print("Please enter valid input")
    if name == "2":
        work = input("Enter (1:- Food, 2:- Exercise)\n")
        try:
            if work == "1":
                rf = input("Type here\n")
                with open("rohan_food.txt", "a") as rh:
                    rh.write(str([str(getdate())])+": "+rf+"\n")
                    print("Write Successfully")
            elif work == "2":
                re = input("Type here\n")
                with open("rohan_exercise.txt", "a") as wf:
                    wf.write(str([str(getdate())])+": "+re+"\n")
                    print("Write Successfully")
        except:
            print("Please enter valid input")
    if name == "3":
        work = input("Enter (1:- Food, 2:- Exercise)\n")
        try:
            if work == "1":
                hf = input("Type here\n")
                with open("hammad_food.txt", "a") as wf:
                    wf.write(str([str(getdate())])+": "+hf+"\n")
                    print("Write Successfully")
            elif work == "2":
                he = input("Type here\n")
                with open("hammad_exerxise.txt", "a") as wf:
                    wf.write(str([str(getdate())])+": "+he+"\n")
                    print("Write Successfully")
        except:
            print("Please enter valid input")


def retrievefile():
    name = input("Enter (1:- Harry, 2:- Rohan, 3:- Hammad):-\n")
    try:
        if name == "1":
            work = input("Enter (1:- food, 2:- Exercise):-\n")
            try:
                if work == "1":
                    with open("harry_food.txt") as rf:
                        for i in rf:
                            print(i, end="")
                elif work == "2":
                    with open("harry_exercise.txt") as rf:
                        for i in rf:
                            print(i, end="")
            except:
                print("Please enter valid input")
    except:
        print("Please enter valid input")

    try:
        if name == "2":
            work = input("Enter (1:- food, 2:- Exercise):-\n")
            try:
                if work == "1":
                    with open("rohan_food.txt") as rf:
                        for i in rf:
                            print(i, end="")
                elif work == "2":
                    with open("rohan_exercise.txt") as rf:
                        for i in rf:
                            print(i, end="")
            except:
                print("Please enter valid input")
    except:
        print("Please enter valid input")

    try:
        if name == "3":
            work = input("Enter (1:- food, 2:- Exercise):-\n")
            try:
                if work == "1":
                    with open("hammad_food.txt") as rf:
                        for i in rf:
                            print(i, end="")
                elif work == "2":
                    with open("hammad_exercise.txt") as rf:
                        for i in rf:
                            print(i, end="")
            except:
                print("Please enter valid input")
    except:
        print("Please enter valid input")


access = input("Enter (1:- write, 2:- retrieve):-\n")
try:
    if access == "1":
        writefile()
    elif access == "2":
        retrievefile()
except:
    print("Please enter valid input")
