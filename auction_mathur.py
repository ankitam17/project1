import random
from bidder_mathur import Bidder

import random
from bidder_mathur import Bidder

class User:
    '''Class to represent a user with a secret probability of clicking an ad.'''

    def __init__(self):
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        self.prob = random.uniform(0, 1)  # Secret click probability

    def __repr__(self):
        return f"User(prob={self.prob:.2f})"

    def __str__(self):
        return f"User with click probability: {self.prob:.2f}"

    def show_ad(self):
        '''Simulate whether user clicks based on probability'''
        return random.random() < self.prob

class Auction:
    '''Class to represent an online second-price ad auction'''

    def __init__(self, users, bidders):
        '''Initialize users, bidders, and dictionary to store balances'''
        self.users = users
        self.bidders = bidders

    def __repr__(self):
        return f"Auction(users={len(self.users)}, bidders={len(self.bidders)})"

    def __str__(self):
        return f"Auction with {len(self.users)} users and {len(self.bidders)} bidders"

    def execute_round(self):
        '''Executes a single round of an auction'''
        user = random.choice(self.users)  # Random user selection
        bids = [(bidder, bidder.bid(id(user))) for bidder in self.bidders]  # Collect bids
        bids.sort(key=lambda x: x[1], reverse=True)  # Sort bidders by bid

        if len(bids) < 2:
            return  # Not enough bidders 

        winning_bidder, highest_bid = bids[0]
        _, second_highest_bid = bids[1]

        price = second_highest_bid  # Second-highest bid 
        clicked = user.show_ad()  # Check clicks

        winning_bidder.notify(True, price, clicked)  # Notify winner
        for bidder, bid_amount in bids[1:]:
            bidder.notify(False, price, False)  # Notify losing bidders
