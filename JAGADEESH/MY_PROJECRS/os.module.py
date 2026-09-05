import random

def higher_lower_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Higher or Lower game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        # Get user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Increment attempt count
        attempts += 1

        # Check the guess against the target number
        if guess < target_number:
            print("Higher! Try again.")
        elif guess > target_number:
            print("Lower! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break

# Run the game
if __name__ == "__main__":
    higher_lower_game()
    




