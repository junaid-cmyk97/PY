def auction():

    bids = {}

    while True:
        bidder_name = input("enter the name bidder:")
        bidder_amount =int(input(f"enter the amount:  /-"))
        if (bidder_amount) <=0:
            continue
            print("please enter a valid number")
            continue

        bids[bidder_name] = bidder_amount 

        people = input("enter if any other bidder yes/no:")
        if people == "yes":
            return bids
        else:
            print("no other bidder")
            break


    if bids:
        highest_bidder = max(bids,key=bids.get)
        highest_bid = bids[highest_bidder]
        print(f"the highest bid is {highest_bidder} with {highest_bid})")
        
a= auction()
print(a)