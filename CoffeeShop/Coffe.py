class CoffeeMachine:
    def __init__(self):
        self.resources = {"water": 500,"milk": 300,"coffee": 100,"money": 0.0}
        self.menu = {"espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 50.0},
                     "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 80.0},
                     "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 100.0}
        }
    def report(self):
        print("\nMachine Report:")
        for item, amount in self.resources.items():
            if item in ["water", "milk"]:
                unit = "ml" 
            elif item == "coffee":
                unit = "g" 
            else:
                "₹"
            print(f"{item.capitalize()}: {amount}{unit}",)
        print()
    def is_resource_sufficient(self, drink):
        for item in ["water", "milk", "coffee"]:
            if self.resources[item] < self.menu[drink][item]:
                print(f"Sorry, not enough {item}.");return False
        return True
    def process_payment(self, cost):
        amount = float(input(f"Please insert ₹{cost:.2f}: "))
        if amount < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        change = amount - cost
        if change > 0:
            print(f"Here is ₹{change:.2f} in change.")
            self.resources["money"] += cost
            return True
    def make_coffee(self, drink):
        for item in ["water", "milk", "coffee"]:
            self.resources[item] -= self.menu[drink][item]
        print(f"Here is your {drink} ☕. Enjoy!\n")
    def run(self):
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
machine = CoffeeMachine();machine.run()

