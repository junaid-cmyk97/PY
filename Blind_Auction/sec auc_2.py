import art

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

def find_largest_bidder(bidders_dictionary):
    largest_bid_price = 0
    winner_name = ""
    for name in bidders_dictionary:
        if bidders_dictionary[name] > largest_bid_price:
            winner_name = name
            largest_bid_price = bidders_dictionary[name]

    print(f"The winner is {winner_name} with a bid of ${largest_bid_price}.")

bidders_dictionary = {}
continue_auction = False
while not continue_auction:
    name = input("What is your name? ")
    price = float(input("What is your bid? $"))
    bidders_dictionary[name] = price

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == "yes":
        print("\n" * 100)
        continue_auction = False
    else:
        continue_auction = True
        find_largest_bidder(bidders_dictionary)