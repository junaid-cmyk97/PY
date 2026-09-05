class Item:
    pay = 0.8


    def __init__(self,name,price,quantity):     #adding ASSERTion to the induvial can print the data for details
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self,x,y):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay


item1 = Item('phone',50,25)

#print(item1.calculate_total_price(item1_price,item1_quantity))

item2 = Item('laptop',150,25)

#print(item2.calculate_total_price(item2_price,item2_quantity))

# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)

# print(item1.calculate_total_price(item1.name,item1.price))
# print(item2.calculate_total_price(item2.name,item2.price))


# print(item1.__dict__)
# print(item2.__dict__)

item1 = Item('phone' ,25,20)
item1.apply_discount()
print(item1.price)

item2 = Item('laptop',150,20)
item2.pay= 0.7
item2.apply_discount()
print(item2.price)

#additional to do ITEMS
item3 = Item('fan',135,16)
item4 = Item('candle',5,88)







