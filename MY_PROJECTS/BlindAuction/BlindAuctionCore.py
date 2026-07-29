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