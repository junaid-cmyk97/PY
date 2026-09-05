
# class market:
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total_cost(self,x,y):
#         return x + y
# bucket_1= market("veg",120,5)
# bucket_2 = market("meat",70,5)
# print(bucket_1.price)
# print(bucket_1.quantity)
# print(bucket_2.price)
# print(bucket_2.quantity)
# # bucket_1_total_price= bucket_1_price * bucket_1_quantity
# # bucket_2_total_price = bucket_2_price * bucket_2_quantity






# Virtual Pet Program for Kids

# class Pet:
#     def __init__(self, name, animal_type):
#         # Initialize pet's name, type, and happiness level
#         self.name = name
#         self.animal_type = animal_type
#         self.happiness = 5  # Scale: 0 (sad) to 10 (very happy)
#
#     def feed(self):
#         """Increase happiness when feeding the pet."""
#         if self.happiness < 10:
#             self.happiness += 1
#             print(f"{self.name} enjoyed the food! Happiness: {self.happiness}")
#         else:
#             print(f"{self.name} is already super happy!")
#
#     def play(self):
#         """Increase happiness when playing with the pet."""
#         if self.happiness < 10:
#             self.happiness += 2
#             if self.happiness > 10:
#                 self.happiness = 10
#             print(f"You played with {self.name}! Happiness: {self.happiness}")
#         else:
#             print(f"{self.name} is already having the best day ever!")
#
#     def talk(self):
#         """Pet talks about how it feels."""
#         if self.happiness > 7:
#             mood = "I'm so happy! 🐾"
#         elif self.happiness > 4:
#             mood = "I'm okay, but let's play!"
#         else:
#             mood = "I'm feeling a bit sad..."
#         print(f"{self.name} says: {mood}")
#
#
# # --- Main Program ---
# try:
#     name = input("What is your pet's name? ")
#     animal_type = input("What kind of animal is it? ")
#
#     my_pet = Pet(name, animal_type)
#
#     while True:
#         print("\nWhat would you like to do?")
#         print("1. Feed")
#         print("2. Play")
#         print("3. Talk")
#         print("4. Quit")
#
#         choice = input("Enter your choice (1-4): ")
#
#         if choice == "1":
#             my_pet.feed()
#         elif choice == "2":
#             my_pet.play()
#         elif choice == "3":
#             my_pet.talk()
#         elif choice == "4":
#             print(f"Goodbye! {my_pet.name} will miss you!")
#             break
#         else:
#             print("Invalid choice. Please enter 1-4.")
#
# except Exception as e:
#     print("Oops! Something went wrong:", e)

#
# class Teacher:
#    pass
# teacher_1 = teacher()
# teacher_1.name = "ben"
# teacher_1.address = "vns"
# print(teacher_1.name)


# x = 88
#
# def my_function():
#    x = 99
#    y = 86
#    print(x)
#    print(y)
#
# my_function()
# print(x)
# print(y)

f = open("myfile.txt","r")
#print(f)
tex  



