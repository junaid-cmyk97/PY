import random
print("🎲 Welcome to Simple Blackjack! 🎲")

player_cards = [random.randint(1, 11), random.randint(1, 11)]
computer_cards = [random.randint(1, 11), random.randint(1, 11)]


print(f"Your cards: {player_cards} (Total: {sum(player_cards)})")

print(f"Computer's first card: {computer_cards[0]}")

while sum(player_cards) < 21:
    choice = input("Do you want another card? (y/n): ").lower()
    if choice == "y":
        player_cards.append(random.randint(1, 11))
        print(f"Your cards: {player_cards} (Total: {sum(player_cards)})")
    else:
        break
    
    
while sum(computer_cards) < 17:
    computer_cards.append(random.randint(1, 11))
    
    
print(f"\nYour total: {sum(player_cards)}")
print(f"Computer's cards: {computer_cards} (Total: {sum(computer_cards)})")



if sum(player_cards) > 21:
    print("💥 You went over 21! Computer wins.")
elif sum(computer_cards) > 21:
    print("💥 Computer went over 21! You win!")
elif sum(player_cards) > sum(computer_cards):
    print("🏆 You win!")
elif sum(player_cards) < sum(computer_cards):
    print("🤖 Computer wins!")
else:
    print("🤝 It's a tie!")

    



