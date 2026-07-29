import random

trails: int = 0
trail = " "
print("select a random number from 1 to 12")

computer_chosen = random.randint(1, 12)
print(computer_chosen)

level_to_choose = input("A: , B: ").upper()

user_chosen = int(input("enter the guess no:"))

levels = ""
def level(trail):
    if level_to_choose == "A":
        print("easy")
        global trails
        trails = 5

    elif level_to_choose == "B":
        print("hard")
        trails = 2
    else:
        print("its not a choice")


trail = level(level_to_choose)
levels = print(f"left {trails}")

while trails > 0:
    user_chosen = int(input("enter the guess no:"))

    if user_chosen == computer_chosen:
        print(f"the guess is correct")
    elif user_chosen > computer_chosen:
        print(f"the guess is greater")
    elif user_chosen < computer_chosen:
        print(f"the guess is smaller")
    else:
        print(f"think once about your trails are losing")
