import random

class Bidder:
    '''Class to represent a bidder in an online second-price ad auction'''
    
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and initializing balance'''
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.balance = 0  # Tracking balance for auction spending

    def __repr__(self):
        return f"Bidder(num_users={self.num_users}, num_rounds={self.num_rounds}, balance={self.balance})"

    def __str__(self):
        return f"Bidder with balance: {self.balance}"

    def bid(self, user_id):
        '''Returns a non-negative bid amount (random for simplicity)'''
        return random.uniform(0, 1)  # Bid between 0 and 1 for example

    def notify(self, auction_winner, price, clicked):
        '''Updates balance based on auction result (price if they won)'''
        if auction_winner:
            self.balance -= price  # Deduct the second-highest bid if won
