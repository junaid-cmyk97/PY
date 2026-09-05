# class Car:
#     def __init__(self, brand, model,year):
#         self.brand = brand
#         self.model = model
#         self.year =  year
#
#     def display(self):
#         print(f"{self.brand} {self.model} {self.year}")
#
# # Example usage
# c = Car("Toyota", "Corolla",1995)
# c.display()


# class School:
#     def present(self,studentname:studentname1,studenttime: studenttime1):
#         if studenttime <= 9:
#            print( f"{studentname} you r present u came @at {studenttime}pm")
#         else:
#             print( f"{studentname} you r absent because ur late ,came@ {studenttime}pm")
#
# my_attendance = School()
# studentname1 = input("please insert your name \n")
# studenttime1 = int(input("please enter ur time \n"))
# print(my_attendance.present(studentname1,studenttime1 ))


# class Mess:
#     def __init__(self,preparation_time =""):
#         self.menu = {"id":20,
#                      "dos":50,
#                      "rice":30,
#                      "chap":25,
#                      "cc":38
#         }
#
#         self.menu_breakfast_items  = {"id", "bos"}
#         self.menu_lunch_items = {"rice", "chap"}
#         self.menu_dinner_items = {"rice", "cc"}
#
#         self.list_time_breakfast = 10
#         self.list_time_lunch = 15
#         self.list_time_dinner = 21
#
#
#         self.preparation_time = preparation_time
#
#     def order(self):
#
#         try:
#             user_visited_time = int(input("please insert your visited time(0-23):"))
#             if not (0<=user_visited_time<=23):
#                 print("invalid time")
#                 return
#             if user_visited_time <= self.list_time_breakfast:
#                 self.take_order(self.menu_breakfast_items,"breakfast")
#             elif user_visited_time <= self.list_time_lunch:
#                 self.take_order(self.menu_lunch_items,"lunch")
#             elif user_visited_time <= self.list_time_dinner:
#                 self.take_order(self.menu_dinner_items ,"dinner")
#             else:
#                 print("invalid time")
#
#         except ValueError:
#             print("invalid time")
#
#     def take_order(self,ava_items,meal_type):
#         print(f"\n{meal_type} menu:")
#         for item in ava_items:
#             print(f"{item}: {self.menu[item]}")
#
#
#         user_choice = input("please insert your choice:")
#         if user_choice in self.menu:
#                 print(f"{user_choice} !please pay {self.menu[user_choice]}")
#         else:
#             print(f"{user_choice} is not available ")
#
#
#
# if __name__ == "__main__":
#     mess = Mess()
#     mess.order()


# class School:
#     def __init__(self,playing_time):
#         self.activities = {
#             "chess",
#             "volleyball",
#             "football",
#             "caroms"
#         }
#
#         self.indoor = {"chess","caroms"}
#         self.outdoor = {"volleyball","football"}
#
#         self.indoor_hour_weekly = 16
#         self.outdoor_hour_weekly = 12
#
#         self.playing_time = playing_time
#
#     def playing(self):
#         try:
#             player_hours  = int(input("Enter your available playing hours this week: :"))
#             if not (0 <= player_hours < 16):
#                 print(f"invalid choice")
#                 return
#
#             if player_hours <= self.indoor_hour_weekly:
#                 print("you can choose from outdoor activities")
#                 available = self.outdoor
#             elif player_hours <= self.outdoor_hour_weekly:
#                 print("you can choose from indoor activities")
#                 available = self.indoor
#             else:
#                 print(f"invalid choice")
#
#         except ValueError:
#             print(f"invalid choice")
#
#
# if __name__ == "__main__":
#     School = School(playing_time=0)
#     School.playing()

# import tkinter as tk
#
# root = tk.Tk()
# root.title("title")
#
# label = tk.Label(root, text="list")
# label.pack(padx=20, pady=20)  # Add padding and pack into window
#
# root.mainloop()


# import tkinter as tk
#
# # Make the main window
# root = tk.Tk()
# root.title("My First Tkinter App")
#
# # Add a label
# label = tk.Label(root, text="Hello, Friend!")
# label.pack()
#
# # Add a button that changes the label text
# def say_hi():
#     label.config(text="You clicked the button!")
#
# button = tk.Button(root, text="Click Me!", command=say_hi)
# button.pack()
#
# # Start the app
# root.mainloop()





#
# import tkinter as tk
# from tkinter import messagebox3
import random
#
#
# def hangman():
#     # A small, kid-friendly word list
#     words = ["cat", "dog", "apple", "ball", "fish", "tree", "book", "milk"]
#
#     # Randomly choose a word
#     secret_word = random.choice(words)
#     guessed_letters = set()
#     attempts_left = len(secret_word) + 2  # Give extra chances for kids
#
#     print("🎯 Welcome to Hangman!")
#     print(f"The word has {len(secret_word)} letters.")
#     print("_ " * len(secret_word))
#
#     while attempts_left > 0:
#         guess = input("\nGuess a letter: ").lower().strip()
#
#         # Validate input
#         if len(guess) != 1 or not guess.isalpha():
#             print("⚠ Please enter a single letter (a-z).")
#             continue
#
#         if guess in guessed_letters:
#             print("🔁 You already guessed that letter.")
#             continue
#
#         guessed_letters.add(guess)
#
#         if guess in secret_word:
#             print("✅ Good guess!")
#         else:
#             attempts_left -= 1
#             print(f"❌ Wrong guess! Attempts left: {attempts_left}")
#
#         # Show current progress
#         display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
#         print("Word:", " ".join(display_word))
#
#         # Check win condition
#         if "_" not in display_word:
#             print("🎉 Congratulations! You guessed the word!")
#             break
#     else:
#         print(f"😢 Out of attempts! The word was '{secret_word}'.")
#
#
# # Run the game
# if __name__ == "__main__":
#     hangman()

#
# import tkinter as tk
# from tkinter import messagebox
# import random
#
# # ---------------------------
# # Game Setup
# # ---------------------------
# WORDS = ["cat", "dog", "apple", "ball", "fish", "tree", "book", "milk"]
#
# # Pick a random word
# secret_word = random.choice(WORDS)
# guessed_letters = set()
# attempts_left = len(secret_word) + 2  # Extra chances for kids
#
# # ---------------------------
# # Functions
# # ---------------------------
# def update_display():
#     """Update the word display and attempts left."""
#     #display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
#     display_word = " ".join(letter)
#     for letter in secret_word:
#         if letter in guessed_letters:
#             parts.append(letter)
#         else:
#             guessed_letters.add(letter)
#     word_label.config(text=display_word)
#     attempts_label.config(text=f"Attempts left: {attempts_left}")
#
# def guess_letter():
#     """Handle a letter guess from the entry box."""
#     global attempts_left
#
#     guess = entry.get().lower().strip()
#     entry.delete(0, tk.END)  # Clear input box
#
#     # Validate input
#     if len(guess) != 1 or not guess.isalpha():
#         messagebox.showwarning("Invalid Input", "Please enter a single letter (a-z).")
#         return
#
#     if guess in guessed_letters:
#         messagebox.showinfo("Already Guessed", f"You already guessed '{guess}'.")
#         return
#
#     guessed_letters.add(guess)
#
#     if guess not in secret_word:
#         attempts_left -= 1
#
#     update_display()
#
#     # Check win condition
#     if all(letter in guessed_letters for letter in secret_word):
#         messagebox.showinfo("You Win!", f"🎉 Congratulations! The word was '{secret_word}'.")
#         root.destroy()
#
#     # Check lose condition
#     elif attempts_left <= 0:
#         messagebox.showinfo("Game Over", f"😢 Out of attempts! The word was '{secret_word}'.")
#         root.destroy()
#
# # ---------------------------
# # Tkinter UI Setup
# # ---------------------------
# root = tk.Tk()
# root.title("Hangman for Kids")
# root.geometry("300x250")
#
# # Word display
# word_label = tk.Label(root, text="_ " * len(secret_word), font=("Arial", 18))
# word_label.pack(pady=10)
#
# # Attempts left
# attempts_label = tk.Label(root, text=f"Attempts left: {attempts_left}", font=("Arial", 12))
# attempts_label.pack(pady=5)
#
# # Entry box
# entry = tk.Entry(root, font=("Arial", 14), justify="center")
# entry.pack(pady=5)
#
# # Guess button
# guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Arial", 12))
# guess_button.pack(pady=10)
#
# # Start display
# update_display()
#
# # Run the app
# root.mainloop()


import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

# -------------------
# CONFIG
# -------------------
CARD_IMAGES = {
    1: "cards/ace.png",
    2: "cards/2.png",
    3: "cards/3.png",
    4: "cards/4.png",
    5: "cards/5.png",
    6: "cards/6.png",
    7: "cards/7.png",
    8: "cards/8.png",
    9: "cards/9.png",
    10: "cards/10.png",
    11: "cards/jack.png"  # Using 11 for Jack/Queen/King for simplicity
}

# -------------------
# GAME LOGIC
# -------------------
def deal_card():
    return random.randint(1, 11)

def update_display():
    # Player cards
    for widget in player_frame.winfo_children():
        widget.destroy()
    for card in player_cards:
        img = Image.open(CARD_IMAGES[card])
        img = img.resize((80, 120))
        photo = ImageTk.PhotoImage(img)
        lbl = tk.Label(player_frame, image=photo)
        lbl.image = photo
        lbl.pack(side=tk.LEFT, padx=5)

    # Computer cards
    for widget in computer_frame.winfo_children():
        widget.destroy()
    for i, card in enumerate(computer_cards):
        if not game_over and i != 0:
            img = Image.open("cards/jack.png")  # Hidden card
        else:
            img = Image.open(CARD_IMAGES[card])
        img = img.resize((80, 120))
        photo = ImageTk.PhotoImage(img)
        lbl = tk.Label(computer_frame, image=photo)
        lbl.image = photo
        lbl.pack(side=tk.LEFT, padx=5)

    player_total_label.config(text=f"Your total: {sum(player_cards)}")
    if game_over:
        computer_total_label.config(text=f"Computer total: {sum(computer_cards)}")
    else:
        computer_total_label.config(text="Computer total: ?")

def hit():
    global game_over
    if not game_over:
        player_cards.append(deal_card())
        if sum(player_cards) > 21:
            end_game("💥 You went over 21! Computer wins.")
        update_display()

def stand():
    global game_over
    if not game_over:
        while sum(computer_cards) < 17:
            computer_cards.append(deal_card())
        if sum(computer_cards) > 21:
            end_game("💥 Computer went over 21! You win!")
        elif sum(player_cards) > sum(computer_cards):
            end_game("🏆 You win!")
        elif sum(player_cards) < sum(computer_cards):
            end_game("🤖 Computer wins!")
        else:
            end_game("🤝 It's a tie!")

def end_game(message):
    global game_over
    game_over = True
    update_display()
    messagebox.showinfo("Game Over", message)

# -------------------
# TKINTER UI
# -------------------
root = tk.Tk()
root.title("🎲 Simple Blackjack 🎲")
root.geometry("600x500")
root.resizable(False, False)

# Frames
computer_frame = tk.Frame(root)
computer_frame.pack(pady=10)

computer_total_label = tk.Label(root, text="Computer total: ?", font=("Arial", 14))
computer_total_label.pack()

player_frame = tk.Frame(root)
player_frame.pack(pady=10)

player_total_label = tk.Label(root, text="Your total: 0", font=("Arial", 14))
player_total_label.pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

hit_button = tk.Button(button_frame, text="Hit", font=("Arial", 14), width=10, command=hit)
hit_button.grid(row=0, column=0, padx=10)

stand_button = tk.Button(button_frame, text="Stand", font=("Arial", 14), width=10, command=stand)
stand_button.grid(row=0, column=1, padx=10)

# -------------------
# START GAME
# -------------------
player_cards = [deal_card(), deal_card()]
computer_cards = [deal_card(), deal_card()]
game_over = False

update_display()

root.mainloop()
