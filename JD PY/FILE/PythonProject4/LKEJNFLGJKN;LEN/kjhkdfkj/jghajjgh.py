import random

print("select a random numberfrom 1 to 12")

computer_choosen = random.randint(1,12)
print(computer_choosen)
print("chose HARD or EASY")

level =" "

user_choosen = input("enter the guess no:")


def level():
    if level_to_choose == A:
        print("easy")
            
        trails = 5
    
    elif level_to_choose == B:
        print("hard")
        trails = 2
    else:
        print("its not a choice")
        
        
trails = level(user_choosen)
level = print(f"left {trails}")


while trails > 0:
    user_choosen = int(input("enter the guess no:"))
    
    if user_choosen == computer_choosen:
        print(f"the guess is correct")
    elif user_choosen > computer_choosen:
        print(f"the guess is greater")
    elif user_choosen < computer_choosen:
        print(f"the guess is smaller")
    else:
        print(f"think once about your trails are losing")
                       


                       
    





