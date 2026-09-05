# class Roads:
#     def __init__(self, name,speed_limit,toll,fine):
#         self.name = name
#         self.speed_limit = speed_limit
#         self.toll = toll
#         self.fine = fine
#
#
#     def highway(self,name,speeed_limit,toll,fine):
#         self.name = "highway"
#         self.speed_limit = 180
#         self.toll = 250
#         self.fine = 5000
#
#         vehicle1_sp = input("enter speed of vehicle: ")
#         if self.speed_limit == 180:
#             print(f"your {vehicle1_sp} is on {self.name}with{self.speed_limit} km/h fine")
#         else:
#             print(f"your {vehicle1_sp} is on {self.name}with{self.speed_limit} km/h is greater than 180 km/h payable {self.fine}")
#
#     def national_ways(self,name,speed_limit,toll,fine):
#         self.name = "national_ways"
#         self.speed_limit = 150
#         self.toll = 200
#         self.fine = 2500
#
#         vehicle2_sp = input("enter speed of vehicle: ")
#         if self.speed_limit == 150:
#             print(f"your {vehicle2_sp} is on {self.name}with{self.speed_limit} km/h fine")
#         else:
#             print(f"your {vehicle2_sp} is on {self.name}with{self.speed_limit} km/h is greater than 150 km/h payable {self.fine}")

# class Roads:
#     # Initialize the default properties of a road
#     def __init__(self, name, speed_limit, toll, fine):
#         self.name = name
#         self.speed_limit = speed_limit
#         self.toll = toll
#         self.fine = fine
#     def check_speed(self):
#         # Get the current speed from the user and convert to integer
#         vehicle_sp = int(input(f"Enter speed of vehicle on {self.name}: "))
#         # Compare user speed against the road's speed limit
#         if vehicle_sp <= self.speed_limit:
#             print(f"Your vehicle is going {vehicle_sp} km/h on {self.name}. Speed is fine.")
#         else:
#             print(f"Your vehicle is going {vehicle_sp} km/h on {self.name}.")
#             print(f"This is greater than the {self.speed_limit} km/h limit. Payable fine: {self.fine}")
# # 1. Create instances (objects) for different road types
# highway_road = Roads("Highway", 180, 250, 5000)
# national_road = Roads("National Way", 150, 200, 2500)
# # 2. Call the methods on the specific objects
# highway_road.check_speed()
# national_road.check_speed()


class Roads:
    def __init__(self, high_roads, speed, fine):
        self.high_roads = high_roads
        self.speed = speed
        self.fine = fine
    def over_speed(self):
        if self.speed >= 250:
            print(f"its fine")
        else:
            print(f"payable fine is {self.fine}")
    def highway_roads(self):
        self.high_roads = "high_roads"
        self.speed = 250
        self.fine = 5000
roads = Roads("highroads", 500, 5000)
roads.over_speed()
roads.highway_roads()


