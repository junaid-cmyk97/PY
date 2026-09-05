


#import random
#print("🎲 Welcome to Simple Blackjack! 🎲")

#player_cards = [random.randint(1, 11), random.randint(1, 11)]
#computer_cards = [random.randint(1, 11), random.randint(1, 11)]


#print(f"Your cards: {player_cards} (Total: {sum(player_cards)})")

#print(f"Computer's first card: {computer_cards[0]}")

#while sum(player_cards) < 21:

#choice = input("Do you want another card? (y/n): ").lower()
#    if choice == "y":
#        player_cards.append(random.randint(1, 11))
#        print(f"Your cards: {player_cards} (Total: {sum(player_cards)})")
#    else:
#        break
    
    
#while sum(computer_cards) < 17:
#    computer_cards.append(random.randint(1, 11))
    
    
#print(f"\nYour total: {sum(player_cards)}")
#print(f"Computer's cards: {computer_cards} (Total: {sum(computer_cards)})")



#if sum(player_cards) > 21:
#    print("💥 You went over 21! Computer wins.")
#elif sum(computer_cards) > 21:
#    print("💥 Computer went over 21! You win!")
#elif sum(player_cards) > sum(computer_cards):
#    print("🏆 You win!")
#elif sum(player_cards) < sum(computer_cards):
#   print("🤖 Computer wins!")
#else:
 #   print("🤝 It's a tie!")
#


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


    



