import random

def hangman():
    # A small, kid-friendly word list
    words = ["cat", "dog", "apple", "ball", "fish", "tree", "book", "milk"]
    
    # Randomly choose a word
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts_left = len(secret_word) + 2  # Give extra chances for kids

    print("🎯 Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters.")
    print("_ " * len(secret_word))

    while attempts_left > 0:
        guess = input("\nGuess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter a single letter (a-z).")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("✅ Good guess!")
        else:
            attempts_left -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts_left}")

        # Show current progress
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print("Word:", " ".join(display_word))

        # Check win condition
        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word!")
            break
    else:
        print(f"😢 Out of attempts! The word was '{secret_word}'.")

# Run the game
if __name__ == "__main__":
    hangman()
    