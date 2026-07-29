bids1 = []
while True:
    user_name = input("enter your name: \n")
    user_bid = input("enter your bid: \n")
    user_confirmation = input("enter your confirmation:yes or no \n").lower()
    bids1.append({"name": user_name, "bid": user_bid})
    
    otherbid_name = input("enter name:")
    otherbid_bid = input("enter bid:")
    
    
    if user_confirmation != "yes":
        break
        print(f"name of {otherbid_name}:")
        print(f"amount{otherbid_bid}:")
    else:
        print(f"no other bidder")
    for bid in bids1:
        print(f" {bid['name']},your bid is {bid['bid']}")
        
        if user_name < otherbid_name:
            print(f"other_bid is winner")
            
        elif user_name > otherbid_name:
            print(f"user_name is winner")
            
        else:
            print(f"its a tie ")
            
            
        print(f"auction completed")
        
        
bids()
