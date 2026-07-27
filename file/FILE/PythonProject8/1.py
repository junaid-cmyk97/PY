import random

print("select a random numberfrom 1 to 12")

computer_choosen = random.randint(1, 12)
print(computer_choosen)
print("chose HARD or EASY")


user_choosen = input("enter the guess no:")
level_to_choose = input("enter the level A or B:")

def level():
    global trails
    if level_to_choose == "A":
        print("easy")

        trails = 5

    elif level_to_choose == "B":
        print("hard")
        trails = 2
    else:
        print("its not a choice")

    return trails


level()
print(trails)

while trails > 0:
    print("THIS IS COMPUTER CHOSEN",computer_choosen)
    user_choosen = int(input("enter the guess no:"))

    if user_choosen == computer_choosen:
        print(f"the guess is correct")
        break

    else:
        print(f"think once about your trails are losing{trails}")

    if user_choosen != computer_choosen:
        trails = trails-1
        if user_choosen > computer_choosen:
            print(f"the guess is greater")
        elif user_choosen < computer_choosen:
            print(f"the guess is smaller")

    if trails <=0:
        print("you lost the game")
        break







