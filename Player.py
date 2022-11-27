from Hand import Hand

class Player:
    """
    The __init__ function is a constructor that initializes the name, balance, and hand attributes
    of the Player class
    
    :param name: The name of the player
    """
    def __init__(self, name):
        self.name = name
        self.balance = 100
        self.hand = Hand(name)

    """
    The function hit() takes in a card and adds it to the hand
    
    :param card: a Card object
    """
    def hit(self, card):
        self.hand.addCard(card)

    """
    This function sets the balance of the account to the value of the parameter balance
    :param balance: The balance of the account
    """
    def setBalance(self, balance):
        self.balance = balance
    
    """
    It returns the balance of the account.
    :return: The balance of the account.
    """
    def getBalance(self):
        return self.balance

    """
    The function resets the hand of the player by setting the cards to an empty list and the hand
    value to 0
    """
    def resetAll(self):
        self.hand.cards = []
        self.hand.handValue = 0