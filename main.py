# Rock - paper - scissor
from random import randint


def win(Choice,comp_choice):
    if Choice == comp_choice:
        print("Draw")
    elif (Choice == 1 and comp_choice == 2) or (Choice == 3 and comp_choice == 1) or (choice == 2 and comp_choice == 3):
        print("Computer Win")
    else:
        print("User Win")


def know_name(x):
    if x == 1:
        res = "Rock"
    elif x == 2:
        res = "Paper"
    else:
        res = "Scissor"
    return res


x1 = 1
while True:
    x1 = int(input("Do you want to play ? "))
    if x1 == 1:
        print("Enter The choice 1 for Rock - 2 for paper - 3 for scissor")
        choice = int(input("Enter your Choice: "))
        if choice < 1 or choice > 3:
            print("invaliddddd number ")
        else:
            choice_name = know_name(choice)
            print("user choice is :", choice_name)
            comp_choice = randint(1, 3)
            comp_name = know_name(comp_choice)
            print("the computer choice is :", comp_name)
            win(choice, comp_choice)
    elif x1 == -1:
        print("Bye Bye")
        break
    else:
        print("invalid number")


