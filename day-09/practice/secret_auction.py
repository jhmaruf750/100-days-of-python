from os import times_result



# #todo 1: ask the user for input
# name=input("waht is your name?:")
# price:int(input("what is your bid?:$"))
#
#
# bids={}
# #todo 2:save data into dictionary {name: price}
# bids["name"]=price
#
#
# #todo 3: whether if new bids need to be added
# should_continue=input("are there any other bidders?Type 'yes' or 'no'.\n")

# todo 4: compare bids in dictionary

def find_highest_bidder(bidding_dictionary):
    winner=""
    hieght_bid=0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>hieght_bid:
            hieght_bid=bid_amount
            winner=bidder


    print(f"The winner is {winner} with a bid of ${hieght_bid}.")



bids={}
continue_bidding=True

while continue_bidding:
    name = input("what is your name?:")
    price= int(input("what is your bid?:$"))
    bids[name] = price
    should_continue = input("are there any other bidders?Type 'yes' or 'no'.\n").lower()
    if should_continue== "no":
        continue_bidding=False
        find_highest_bidder(bids)
    elif should_continue=="yes":
        print("\n"*20)


