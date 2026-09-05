#resourse
#menu
#report
#resouse suffiency
#paymnet
#making proces
#main loop



class coffeeMachine():
    def __init__(self):
        self.resources = {"coffee_pow":100,"milk":200,"water":300}



        self.menu = {"espresso": {"water":45,"milk":45,"coffee_pow":45,"price":240},
                     "latte": {"water":50,"milk":50,"coffee_pow":50,"price":350},
                     "cap": {"water":60,"milk":60,"coffee_pow":60,"price":450},

        }


    def report(self):
        for item in self.menu:
            if item,amount in self.resources.items():
                unit = "ml"
            elif item == "coffee_pow":
                unit = "grams"
            else:
                 "/-"
            print(f"{item}: {unit}")


    def is_resources_sufficient(self,drink):
        for item in["water","milk","coffee_pow"]:
            if self.resources[item] < self.menu[drink][item]:
                print(f"{item} take time wait for five mins")
                return False
        return True

    def payment(self,cost):
        money = float(input(f"share some {cost}"))
        if money < cost:
            print("please share the as per menu")
            change = money - cost
        elif money > cost:
            print("here is your {change}")
        else:
            money = cost
            print(f"thank you")


    def making_process(self,drink):
        for item in ["water","milk","coffee_pow"]:
            self.resources[item] -= self.menu[item][drink]
        print(f"enjoy the {drink}")


    def run(self):
        while True:
            user_choice = input("enter your choice")
            if user_choice == "off":
                print(f"switch of the machine")
                break
            elif user_choice == "report":
                self.report()
            elif user_choice in self.menu:
                if self.is_resources_sufficient(user_choice):
                    if self.payment(user_choice):
                        self.making_process(user_choice)
            else:
                print("try again")
coffeeMachine().run()










