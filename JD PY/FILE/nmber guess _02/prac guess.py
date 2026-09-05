import random

computer_guess = random.randint(1,30)
print(computer_guess)

player_guess = int(input("Enter your guess: "))


if player_guess == computer_guess:
    print("You guessed right")
elif player_guess <  computer_guess:
    print("You guess is lesser than computer_guess")
else:
    print("losssssst")


height = 5
weight = 80 

user_input = int(input("enter height:  ft & weight:   kgs"))
















