import random
from bidder_mathur import Bidder

class User:
    '''Class to represent a user with a secret probability of clicking an ad.'''

    def __init__(self):
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        self.prob = random.uniform(0, 1)

    def __repr__(self):
        return f"User(prob={self.prob:.2f})"
        '''User object with secret probability'''       

    def __str__(self):
        return f"User with click probability: {self.prob:.2f}"
        '''User object with a secret likelihood of clicking on an ad'''

    def show_ad(self):
        '''Returns True to represent the user clicking on an ad or False otherwise'''
        return random.random() < self.prob

class Auction:
    '''Class to represent an online second-price ad auction'''
    
    def __init__(self, users, bidders):
        '''Initializing users, bidders, and dictionary to store balances for each bidder in the auction'''
        self.users = users
        self.bidders = bidders
        self.balances = {bidder: bidder.balance for bidder in bidders}

    def __repr__(self):
        '''Return auction object with users and qualified bidders'''
        return f"Auction with: {len(self.users)} users and {len(self.bidders)} bidders"

    def __str__(self):
        '''Return auction object with users and qualified bidders'''
        return f"Auction with {len(self.users)} users and {len(self.bidders)} bidders"
    
    def execute_round(self):
        '''Executes a single round of an auction, completing the following steps:
            - random user selection
            - bids from every qualified bidder in the auction
            - selection of winning bidder based on maximum bid
            - selection of actual price (second-highest bid)
            - showing ad to user and finding out whether or not they click
            - notifying winning bidder of price and user outcome and updating balance
            - notifying losing bidders of price'''
        #random user selection
        user = random.choice(self.users)
        #bids for qualified bidders
        bids = [(bidder, bidder.bid(user)) for bidder in self.bidders]
        sorted_bids = sorted(bids, key=lambda x: x[1], reverse=True)
    
        #selection of winning bid and second highest bid
        if len(sorted_bids) > 1:
            winner, winning_bid = sorted_bids[0]
            _, second_highest_bid = sorted_bids[1]
            price = second_highest_bid
        elif sorted_bids:
            winner, winning_bid = sorted_bids[0]
            price = winning_bid  # Only one bid, so winner pays their bid amount
        else:
            print("No bidders participated.")
            return
        #showing ad to user and finding whether they clicked
        clicked = user.show_ad()
        #notify winners
        winner.notify(auction_winner=True, price=price, clicked=clicked)
        #notify losers of the price
        for bidder, bid in sorted_bids[1:]:
            bidder.notify(auction_winner=False, price=0, clicked=False)
            
        print(f"User {user} saw the ad. Winning Bidder: {winning_bidder.name} with bid: {winning_bid:.2f}")
        print(f"Charged price: {second_highest_bid:.2f}, User Clicked: {user_clicked}")
        print(f"{winning_bidder.name}'s new balance: {winning_bidder.balance:.2f}")




        
