# def auction():
#
#     bids= []
#
#     while True:
#         bid= int(input("Enter bid in amount: "))
#         if bid >= 0:
#             print(f"amount for bid_1 is {bid}")
#         else:
#             print("enter a valid amount")
#
#         other_bid= input("raise for other bid in amount: \n yes/no")
#         if other_bid == "yes":
#             print(input("Enter bid_2 in amount: "))
#             return
#
#         else:
#             print("no {other_bid} is entered")
# auction()


bids1 = []
while True:
    user_name = input("enter your name: \n")
    user_bid = input("enter your bid: \n")
    user_confirmation = input("enter your confirmation:yes or no \n").lower()
    bids1.append({"name": user_name, "bid": user_bid})
    if user_confirmation != "yes":
        break
    for bid in bids1:
        print(f" {bid['name']},your bid is {bid['bid']}")





# def auction():
#     bids = {}  # Dictionary to store bidder names and their bids
#
#     print("=== Welcome to the Auction Program ===")
#     while True:
#         name = input("Enter bidder's name: ").strip()
#
#         try:
#             bid = float(input(f"Enter {name}'s bid amount: ₹"))
#             if bid <= 10:
#                 print("Bid must be greater than zero. Try again.")
#                 continue
#         except ValueError:
#             print("Invalid bid amount. Please enter a number.")
#             continue
#
#         bids[name] = bid
#
#         # Ask if there are more bidders
#         more = input("Are there more bidders? (yes/no): ").strip().lower()
#         if more in ("yes","y"):
#             break
#
#     # Determine the highest bidder
#     if bids:
#         highest_bidder = max(bids, key=bids.get)
#         highest_bid = bids[highest_bidder]
#         print("\n=== Auction Result ===")
#         print(f"Winner: {highest_bidder} with a bid of ₹{highest_bid:.2f}")
#     else:
#         print("No bids were placed.")
#
# if __name__ == "__main__":
#     auction()