class tiff():

    def __init__(self):       # call resources to process
        self.resources = {"flour_A":100,"flour_B":200,"flour_C":300,"water":400,"money":0}  #after resources and menu

        self.menu = {"idly": {"flour_A":25,"flour_B":50,"flour_C":50,"water":50,"price":15},
                      "dosa": {"flour_A":25,"flour_B":50,"flour_C":50,"water":50,"price":20},
                      "bonda": {"flour_A":25,"flour_B":50,"flour_C":50,"water":50,"price":30},
        }

    def report(self):
        print("report:")
        for item,user_money in self.resources.items():
            if item in ["flour_A","flour_B","flour_C"]:
                unit = "grams"
            elif item == "water":
                unit = "ml"
            else:
               unit = "₹"
            print(f"{item}: {user_money}{unit}")

    def is_resources_sufficient(self,food):
        for item in ["flour_A","flour_B","flour_C"]:
            if self.resources[item] < self.menu[food][item]:
                print(f"try again")
                return False
        return True

    def payment(self,price):
        user_money = float(input("please insert {price}"))

        if user_money < price:
            print(f"sorry,its not enough money")
            return False
        change = user_money-price
        if change >0:
            print(f"here is the {change}")
            self.resources["money"] += price
            return True

    def making(self,food):
        for item in ["flour_A","flour_B","flour_C"]:
            self.resources[item] -= self.menu[food][item]
        print(f"enjoy the {food}")


    def panama(self):
        while True:
            user_choice = input("please insert your choice \n")
            if user_choice == "off":
                print("out of availability")
                break
            elif user_choice == "report":
                self.report()
            elif user_choice in self.menu:
                if self.is_resources_sufficient(user_choice):
                    if self.payment(self.menu[user_choice]["price"]):
                        self.making(user_choice)

tiff().panama()




