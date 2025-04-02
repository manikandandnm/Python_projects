name = input("Enter your name: ")
bid = int(input("Enter You bid: "))
list_of_bids = {
    name:bid,
}

def find_high(list_of_bid):
    last_high = 0
    won = ""
    for item in list_of_bids:
        if list_of_bids[item] > last_high:
            last_high = list_of_bids[item]
            won = item
    print(f"Highest bid is {last_high} and {won} Won!")
keep_bidding = True
while keep_bidding:
    proceed = input("Any other person wants to bid? yes / no").lower()
    if proceed == "no":
        keep_bidding = False
        find_high(list_of_bids)
    else:
        print("\n" * 20)
        name = input("Enter your name: ")
        bid = int(input("Enter You bid: "))
        list_of_bids[name]= bid
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


