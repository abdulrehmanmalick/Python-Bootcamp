import os

bidders = {}
runagain = True


def welcomeMsg():
    print('Welcome to Secret Auction Program\n')
    print('\n')

def addtoDictionary(bidder_name, bidding_price):
    bidders[bidder_name] =  bidding_price

def highestBidder():
    highest_bid = 0
    highest_bidder = None
    
    for name, bid in bidders.items():
        bid_int = int(bid)
        if bid_int > highest_bid:
            highest_bid = bid_int
            highest_bidder = name
    
    if highest_bidder is not None:
        print(f'Highest Bid is {highest_bid} by {highest_bidder}')
    else:
        print('No bidders found')



welcomeMsg()
while runagain:
    name = input('What is your name? \n')
    bidprice = input('What is your bid?\n')

    addtoDictionary(bidder_name=name, bidding_price=bidprice)

    decision = input('Is there any other bidder(Y/N)?\n').lower()

    if decision == 'n':
        runagain = False
    else:
        os.system('cls')
        

highestBidder()


    
