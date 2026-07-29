import random

print("🎯 Welcome to the Number Treasure Hunt!")
print("I'm thinking of a number between 1 and 20... Can you find it?")

# Computer picks a secret number
secret_number = random.randint(1, 20)

# Player chooses difficulty
difficulty = input("Choose EASY (10 guesses) or HARD (5 guesses): ").lower()

def set_lives(level):
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("Oops! That's not a choice. I'll give you EASY mode.")
        return 10

lives = set_lives(difficulty)
print(f"🕹 You have {lives} guesses. Let's go!")

# Game loop
while lives > 0:
    guess = int(input("🔍 What's your guess? "))

    if guess == secret_number:
        print("🎉 Hooray! You found the treasure!")
        break
    elif guess > secret_number:
        print("📉 Too high! Try a smaller number.")
    else:
        print("📈 Too low! Try a bigger number.")

    lives -= 1

    if lives > 0:
        print(f"❤️ You have {lives} guesses left.")
    else:
        print(f"💀 Oh no! You ran out of guesses. The treasure number was {secret_number}.")