import art
print(art.logo)

# compare bids in dictionary
def find_the_highest_bidder(bidding_dictionary):

    # set an empty string for winner
    winner = ""

    # set an empty int for highest bidder
    highest_bid = 0

    # check every key in this bidding dictionary
    for bidder in bidding_dictionary:
        # bid amount = bidding dictionary[key] which is equivalent to bids[name] = price which also equivalent to bids["kai"] = 500
        bid_amount = bidding_dictionary[bidder]

        # check the bid amount of every key if it is higher than another
        if bid_amount > highest_bid:
            # set the current bid amount to become the highest
            highest_bid = bid_amount
            # the winner will become the current bid amount's bidder which is bidding_dictionary[bidder] = bid_amount
            winner = bidder

    # finally print out the final winner outside of the for loop with its highest bid
    print(f"The winner is {winner} with a bid of £{highest_bid}")

# set an empty dictionary, always set the empty dictionary to be outside of a loop so it does not get refreshed away from a loop and store all the records
bids = {}
continue_bidding = True

while continue_bidding:

    name = input("What is your name?: ")
    price = int(input("What is your bid?: £"))

    # storing name as left key and price as right value connected to left
    bids[name] = price

    more_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if more_bidder == "no":
        continue_bidding = False
        # set the function to link with the dictionary of the input
        find_the_highest_bidder(bids)
    
    elif more_bidder == "yes":
        print("\n" * 20)