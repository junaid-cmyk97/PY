import tkinter as tk
import random

# Hangman stages (ASCII art)
stages = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """
]

# Word list
word_list = ["aardvark", "baboon", "camel", "python", "hangman"]
chosen_word = random.choice(word_list)
guessed_letters = []
lives = len(stages) - 1

# Tkinter window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("500x500")
root.resizable(False, False)

# Display labels
stage_label = tk.Label(root, text=stages[lives], font=("Courier", 12), justify="left")
stage_label.pack(pady=10)

word_display = tk.StringVar()
word_display.set("_ " * len(chosen_word))
word_label = tk.Label(root, textvariable=word_display, font=("Helvetica", 20))
word_label.pack(pady=10)

status_label = tk.Label(root, text=f"Lives: {lives}", font=("Helvetica", 14))
status_label.pack(pady=5)

message_label = tk.Label(root, text="", font=("Helvetica", 14), fg="blue")
message_label.pack(pady=5)

# Function to update the game state
def guess_letter(letter):
    global lives
    if letter in guessed_letters:
        message_label.config(text="You already guessed that letter!")
        return

    guessed_letters.append(letter)

    display = ""
    for l in chosen_word:
        if l in guessed_letters:
            display += l + " "
        else:
            display += "_ "

    word_display.set(display.strip())

    if letter not in chosen_word:
        lives -= 1
        stage_label.config(text=stages[lives])
        status_label.config(text=f"Lives: {lives}")
        message_label.config(text=f"Wrong guess: {letter}")

    # Win condition
    if "_" not in display:
        message_label.config(text="🎉 You win!", fg="green")
        disable_buttons()

    # Lose condition
    if lives == 0:
        message_label.config(text=f"💀 You lost! Word was '{chosen_word}'", fg="red")
        disable_buttons()

# Disable all buttons after game ends
def disable_buttons():
    for btn in letter_buttons:
        btn.config(state="disabled")

# Create letter buttons
letters_frame = tk.Frame(root)
letters_frame.pack(pady=10)

letter_buttons = []
for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    btn = tk.Button(
        letters_frame,
        text=letter.upper(),
        width=4,
        height=2,
        command=lambda l=letter: guess_letter(l)
    )
    btn.grid(row=i // 9, column=i % 9, padx=2, pady=2)
    letter_buttons.append(btn)

root.mainloop()