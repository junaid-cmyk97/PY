print("☕ Welcome to the Coffee Machine! ☕")
print("1. Espresso\n2. Latte\n3. Cappuccino\n4. Hot Chocolate")

choice = input("Pick a drink (1-4): ")

drinks = {"1": "Espresso", "2": "Latte", "3": "Cappuccino", "4": "Hot Chocolate"}

if choice in drinks:
    print(f"Making your {drinks[choice]}... Done! 😋")
else:
    print("Oops! That's not on the menu.")

