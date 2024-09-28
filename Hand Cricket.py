import random
def main():
    print("*********Hand Cricket!!!!*********")
    while True:
        try:
            toss_choice = input("Type in HEADS or TAILS for a toss: ").upper()
            if toss_choice not in ["HEADS", "TAILS"]:
                raise ValueError
            else:
                toss(toss_choice)
                break
        except ValueError:
            print("Invalid Keyword. Type in HEADS or TAILS ")

def toss(t):
    toss_gen = random.choice(["HEADS", "TAILS"])
    print(f"Toss result: It's {toss_gen}")
    if t == toss_gen:
        b = batorball("user_choice")
    else:
        b = batorball("comp_choice")


def batorball(c):
    if c == "user_choice":
        print("You won the toss!!!, Let's play!!")
        x = input("Choose to BAT or BALL: ").upper()
        if x == "BAT":
            bat()
        elif x == "BALL":
            ball()
        else:
            print("Wrong Keyword ")
    elif c == "comp_choice":
        print("I won the toss!!! Let's play!!")
        r = random.choice(["BAT", "BALL"])
        print("I choose to ", r)
        if r == "BAT":
            ball()
        elif r == "BALL":
            bat()
        else:
            print("Wrong Keyword ")


def bat(sysscore=None):
    userscore = 0
    while True:
        try:
            compbat = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
            userbat = getnum("bat")
            print(f"        My balling: {compbat}")
            userscore += userbat
            if sysscore == None:
                if userbat == compbat:
                    print("It's a WICKET!!!!")
                    raise ValueError
            else:
                if compbat == userbat:
                    print("It's a WICKET!!!!")
                    raise ValueError
                elif userscore >= sysscore:
                    raise ValueError
        except ValueError:
            print("Your Batting Ends!!")
            if sysscore == None:
                print(f"Runs I have to score is {userscore}")
                ball(userscore)
                break
            else:
                if userscore >= sysscore:
                    print("You Won!!")
                    print(f"Runs Left for me to win {userscore - sysscore } ")
                    break
                else:
                    print("I Won!!")
                    print(f"Runs Left for you to win {sysscore - userscore} ")
                    break

def ball(userscore=None):
    sysscore = 0
    while True:
        try:
            sysbat = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
            userball = getnum("ball")
            print(f"        My batting: {sysbat}")
            sysscore += sysbat
            if userscore == None:
                if sysbat == userball:
                    print("It's a WICKET!!!!")
                    raise ValueError
            else:
                if sysbat == userball:
                    print("It's a WICKET!!!!")
                    raise ValueError
                elif sysscore >= userscore:
                    raise ValueError
        except ValueError:
            print("My Batting Ends!!")
            if userscore == None:
                print(f"Runs you have to score is {sysscore}")
                bat(sysscore)
                break
            else:
                if sysscore >= userscore:
                    print("I Won!!")
                    break
                elif userscore >= sysscore:
                    print(f"Runs Left for me to win {userscore - sysscore} ")
                    print("You Won!!")
                    break

def getnum(b):
    if b == "ball":
        while True:
            try:
                userbat = int(input("Enter Your Balling: "))
                if userbat not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    raise ValueError
                else:
                    return userbat
            except ValueError:
                print("Enter your batting runs from 1 to 9 only.")
    elif b == "bat":
        while True:
            try:
                userbat = int(input("Enter Your Batting: "))
                if userbat not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    raise ValueError
                else:
                    return userbat
            except ValueError:
                print("Enter your batting runs from 1 to 9 only.")


if __name__ == "__main__":
    main()

