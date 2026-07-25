
import random


def hangman():
    # Simple, kid-friendly word list
    words = ["cat", "dog", "apple", "ball", "fish", "tree", "sun", "star", "milk", "book"]

    # Randomly choose a word
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts_left = len(secret_word) + 2  # Give extra chances for kids

    print("🎯 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"The word has {len(secret_word)} letters.")

    # Game loop
    while attempts_left > 0:
        # Show current progress
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print("\nWord:", " ".join(display_word))
        print(f"Attempts left: {attempts_left}")

        # Get user input
        guess = input("Enter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter only one letter (a-z).")
            continue

        # Check if already guessed
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        # Add guess to guessed letters
        guessed_letters.add(guess)

        # Check guess
        if guess in secret_word:
            print("✅ Good guess!")
            if all(letter in guessed_letters for letter in secret_word):
                print(f"🎉 Congratulations! You guessed the word: {secret_word}")
                break
        else:
            print("❌ Oops! That letter is not in the word.")
            attempts_left -= 1

    else:
        print(f"😢 Out of attempts! The word was: {secret_word}")


# Run the game
if __name__ == "__main__":
    hangman()