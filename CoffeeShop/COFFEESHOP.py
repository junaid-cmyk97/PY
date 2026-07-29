
class CoffeeShop:
    def __init__(self, name):
        self.name = name
        # Menu with prices
        self.menu = {
            "espresso": 12000,
            "latte": 15000,
            "cappuccino": 14000,
            "americano": 10000
        }
        # Inventory (cups available for each drink)
        self.inventory = {
            "espresso": 10,
            "latte": 8,
            "cappuccino": 6,
            "americano": 12
        }
        self.total_sales = 0

    def display_menu(self):
        print(f"\nWelcome to {self.name}!")
        print("------ MENU ------")
        for item, price in self.menu.items():
            print(f"{item.capitalize():<12} ₹{price}")
        print("------------------")

    def take_order(self):
        order_list = {}
        while True:
            drink = input("\nEnter drink name (or 'done' to finish): ").strip().lower()
            if drink == "done":
                break
            if drink not in self.menu:
                print("❌ Sorry, we don't have that item.")
                continue
            try:
                qty = int(input(f"Enter quantity for {drink}: "))
                if qty <= 0:
                    print("❌ Quantity must be positive.")
                    continue
                if qty > self.inventory[drink]:
                    print(f"❌ Only {self.inventory[drink]} available.")
                    continue
                order_list[drink] = order_list.get(drink, 0) + qty
            except ValueError:
                print("❌ Please enter a valid number.")
        return order_list

    def process_order(self, order_list):
        if not order_list:
            print("No items ordered.")
            return
        total = 0
        print("\n------ BILL ------")
        for drink, qty in order_list.items():
            price = self.menu[drink] * qty
            total += price
            self.inventory[drink] -= qty
            print(f"{drink.capitalize():<12} x{qty} = ₹{price}")
        print("------------------")
        print(f"Total: ₹{total}")
        self.total_sales += total

    def show_inventory(self):
        print("\nCurrent Inventory:")
        for drink, qty in self.inventory.items():
            print(f"{drink.capitalize():<12} {qty} cups")

    def show_sales(self):
        print(f"\nTotal Sales: ₹{self.total_sales}")


# Main program
if __name__ == "__main__":
    shop = CoffeeShop("Brew & Beans")
    while True:
        shop.display_menu()
        order = shop.take_order()
        shop.process_order(order)
        shop.show_inventory()
        cont = input("\nTake another order? (y/n): ").strip().lower()
        if cont != 'y':
            shop.show_sales()
            print("Thank you for visiting!")
            break