import random

class Bidder:
    '''Class to represent a bidder in an online second-price ad auction'''
    
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.round_counter = 0
        self.balance = 100.0 #starting balance
        

    def __repr__(self):
        '''Return Bidder object'''
        return f"Bidder(num_users={self.num_users}, num_rounds={self.num_rounds}, balance={self.balance})"
    

    def __str__(self):
        '''Return Bidder object'''
        return f"Bidder with {self.num_users} users, {self.num_rounds} rounds, balance: ${self.balance}"
    

    def bid(self, user_id):
        '''Returns a non-negative bid amount'''
        bid_amount = random.uniform(0.5, 2.0)  # Random bid between 0.5 and 2.0
        print(f"Bidder places a bid of ${bid_amount:.2f} for User {user_id}")
        return bid_amount
        

    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        self.round_counter += 1
        if auction_winner:
            self.balance -= price
            result = "clicked" if clicked else "did not click"
            print(f"Round {self.round_counter}: Won auction at ${price:.2f}. User {result}. Balance: ${self.balance:.2f}")
        else:
            print(f"Round {self.round_counter}: Lost auction. Balance: ${self.balance:.2f}")
