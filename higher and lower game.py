import random

def higher_and_lower_game():
    number_to_guess = random.randint(1,22)
    print(number_to_guess)

    attempts = 0


    while True:
        try:
            guess = int(input("the number is: "))
            print(guess)
        except ValueError:
            print(f"please enter the correct number: {number_to_guess}")
            continue

        attempts += 1

        if number_to_guess < guess:
            print(f"your guess is too low")
        elif number_to_guess > guess:
            print(f"your guess is too high")
        else:
            print(f"your guess is correct")

higher_and_lower_game()







