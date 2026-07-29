class CoffeeMachine:
    def __init__(self):
        # Initial resources in the machine
        self.resources = {
            "water": 500,   # ml
            "milk": 300,    # ml
            "coffee": 100,  # g
            "money": 0.0    # ₹
        }
        # Menu with ingredient requirements and cost
        self.menu = {
            "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 50.0},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 80.0},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 100.0}
        }

    def report(self):
        """Display current resources."""
        print("\nMachine Report:")
        for item, amount in self.resources.items():
            unit = "ml" if item in ["water", "milk"] else ("g" if item == "coffee" else "₹")
            print(f"{item.capitalize()}: {amount}{unit}")
        print()

    def is_resource_sufficient(self, drink):
        """Check if enough resources are available."""
        for item in ["water", "milk", "coffee"]:
            if self.resources[item] < self.menu[drink][item]:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def process_payment(self, cost):
        """Handle payment and return True if successful."""
        try:
            amount = float(input(f"Please insert ₹{cost:.2f}: "))
            if amount < cost:
                print("Sorry, that's not enough money. Money refunded.")
                return False
            change = amount - cost
            if change > 0:
                print(f"Here is ₹{change:.2f} in change.")
            self.resources["money"] += cost
            return True
        except ValueError:
            print("Invalid input. Payment cancelled.")
            return False

    def make_coffee(self, drink):
        """Deduct resources and serve coffee."""
        for item in ["water", "milk", "coffee"]:
            self.resources[item] -= self.menu[drink][item]
        print(f"Here is your {drink} ☕. Enjoy!\n")

    def run(self):
        """Main loop for the coffee machine."""
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
            if choice == "off":
                print("Turning off the coffee machine. Goodbye!")
                break
            elif choice == "report":
                self.report()
            elif choice in self.menu:
                if self.is_resource_sufficient(choice):
                    if self.process_payment(self.menu[choice]["cost"]):
                        self.make_coffee(choice)
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.run()

# MENU = {
#    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
#    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
#    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
# }
# resources = {"water": 300, "milk": 200, "coffee": 100}
# profit = 0
# def is_resource_sufficient(order_ingredients):
#    for item in order_ingredients:
#        if order_ingredients[item] > resources[item]:
#            print(f"Sorry, there is not enough {item}.")
#            return False
#    return True
# def process_coins():
#    print("Insert coins.")
#    total = int(input("Quarters: ")) * 0.25
#    total += int(input("Dimes: ")) * 0.10
#    total += int(input("Nickels: ")) * 0.05
#    total += int(input("Pennies: ")) * 0.01
#    return total
# def make_coffee(drink_name, order_ingredients):
#    for item in order_ingredients:
#        resources[item] -= order_ingredients[item]
#    print(f"Here is your {drink_name} ☕️.")
# def coffee_machine():
#    global profit
#    while True:
#        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#        if choice == "off":
#            break
#        elif choice == "report":
#            print(f"Water: {resources['water']}ml")
#            print(f"Milk: {resources['milk']}ml")
#            print(f"Coffee: {resources['coffee']}g")
#            print(f"Money: ${profit}")
#        elif choice in MENU:
#            drink = MENU[choice]
#            if is_resource_sufficient(drink["ingredients"]):
#                payment = process_coins()
#                if payment >= drink["cost"]:
#                    profit += drink["cost"]
#                    change = round(payment - drink["cost"], 2)
#                    print(f"Here is ${change} in change.")
#                    make_coffee(choice, drink["ingredients"])
#                else:
#                    print("Sorry, that's not enough money. Money refunded.")
#        else:
#            print("Invalid choice.")
# coffee_machine()

