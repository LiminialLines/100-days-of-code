# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)
def auctioneer():
    bidding = True
    partners = {}
    while bidding:
        name = input("Howdy partner! What's your rootin tootin daggone name?\n")
        bid = int(input("And how many of the good government's dollars are you bidding today?\n"))
        partners[name] = bid
        more = input("Any other bidders? yes/no\n").lower()
        if more == "no":
            bidding = False
    return partners
bids = auctioneer()
winner = max(bids, key=bids.get)
highest_bid = bids[winner]

print(f"Winner: {winner} with ${highest_bid}")