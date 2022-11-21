from Hand import Hand

class Player:

    def __init__(self, name):
        self.name = name
        self.balance = 100
        self.hand = Hand(name)

    def hit(self, card):
        self.hand.addCard(card)

    def setBalance(self, balance):
        self.balance = balance

    def getBalance(self):
        return self.balance