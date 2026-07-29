def auction():

    bids = {}

    while True:
        name = input("enter the name bidder:")

        try:
            bid = float("enter the name bidder:  and amount:  ₹")

            if bid <=0:
                print("please enter a positive number")
                continue

        except ValueError:
            print("please enter a valid number")
            continue

        bids[name] = bid

        people = input("enter if any other bidder yes/no:")
        if people == "yes":
            return bids
        else:
            print("no other bidder")
            continue


        if bids:
            highest_bidder = max(bids,key=bids.get)
            highest_bid = bids[highest_bidder]
            print(f"the highest bid is {highest_bidder} with {highest_bidd})")
            
auction()






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