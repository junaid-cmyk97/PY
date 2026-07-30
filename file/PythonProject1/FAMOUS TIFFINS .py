class FAMOUS_TIFFINS:
    def __init__(self):
        # ADD RESOURCES IN AVAIL
        self.resources={
            "maida flour": 80,
            "gram flour" :20,
            "white flour":20,
            "water":300
        }

        # resources that are used for items in menu

        self.menu = {
            "dosa":{"water":50,"white flour":5,"maida flour":5,"price":25},
            "idly":{"white flour":5,"maida flour":5,"water":20,"price":30},
            "bonda":{"maida flour":30,"white gram":5,"water":30,"price":40}

        }

    def report(self):
        print("tiffin:")

        for item,amount in self.resources:
            if item in ["maida flour","gram flour","white flour"]:
                unit = "gms"
            else:
                if item == "water":
                    unit = "ml"
                else:
                    unit = "/-"

            print(f"{item.capitalize()}: {amount}{unit}")

    def is_resource_sufficiency(self, tiff):

        for item in ["maida flour","gram flour","white flour","water"]:
            if self.resources[item] < self.menu[tiff][item]:
                print(f"out of resources for {item}")
                return False
        return True

    def payment_type(self,price):
        amount = input("user cash :")
        if amount < price:
            print(f"{price} is less than /-{amount}")
        elif amount > price:
            print(f"{price} is greater than /-{amount}")
        else:
            print(f"{price} is equal to /-{amount}")

    def making_process(self,tiff):
        for item in ["maida flour","gram flour","white flour"]:
            self.resources[item] -= self.menu[item][tiff]
            print(f"its your{tiff}")




    def run(self):
        #main loop
        choice = input("please choose a idly/dosa/bonda \n")
        if choice == "no resource available":
            print(f"please come later")
        elif choice == "report":
            self.report()
        elif choice in self.menu:
            if self.resource_sufficiency(choice):
                if self.payment_type(self.menu[choice]["price"]):
                    choice = self.menu[choice]["price"]
        else:
            print("please choose a resource")

FAMOUS_TIFFINS().run()














