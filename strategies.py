class Player:
    def __init__(self, balance):
        self.balance = balance
        self.bet = 0
    def round(self, won):
        if self.bet > self.balance:
            self.bet = self.balance
        if won:
            self.balance += self.bet
        else:
            self.balance -= self.bet

"""
Martingale 
    First bet any amount
    If you win: bet the initial amount
    If you lose: double the bet next round
"""
class Martingale(Player):
    def __init__(self, balance):
        Player.__init__(self, balance)
        self.initial_bet = 0.05*balance
        self.bet = self.initial_bet
    def round(self, won):
        Player.round(self, won)
        if (won):
            self.bet *= 2
        else:
            self.bet = self.initial_bet

"""
D'Alembert 
    Divide your bankroll into betting units (1% is recommended)
    First bet 5 units
    If you win: subtract one unit from your bet (minimum bet of 1 unit)
    If you lose: add one unit to your bet
"""
class Alembert(Player):
    def __init__(self, balance):
        Player.__init__(self, balance)
        self.unit = 0.01*balance
        self.bet = 5*self.unit
    def round(self, won):
        Player.round(self, won)
        if (won):
            self.bet -= self.unit
            if self.bet < self.unit: 
                self.bet = self.unit
        else:
            self.bet += self.unit

"""
Parlay (Reverse Martingale)
    First bet any amount
    If you win: double the bet next round
    If you double: bet the initial amount
"""
class Parlay(Player):
    def __init__(self, balance):
        Player.__init__(self, balance)
        self.initial_bet = 0.05*balance
        self.bet = self.initial_bet
    def round(self, won):
        Player.round(self, won)
        if (won):
            self.bet *= 2
        else:
            self.bet = self.initial_bet