from Deck import Deck
from Player import Player
from Hand import Hand

class Main:
    deck1 = Deck()
    deck2 = Deck()

    def __init__(self):
        print("\n===============================")
        print("=     Welcome to BlackJack    =")
        print("===============================\n")
        self.deck = Deck()

    def preparationStage(self):
        self.queryPlayerName()
        self.createPlayer()
        self.startGame()

    def createPlayer(self):
        self.player = Player(self.name)
        self.dealer = Player("Dealer")

    def queryPlayerName(self):
        self.name = input("Enter your name: ")
    
    def queryBet(self):
        self.bet = int(input("How much is your bet: "))

        while(self.bet > self.player.getBalance()):
            print("Insufficient balance! Your remaining balance is " + str(self.player.getBalance()))
            print("\n===============================\n")
            self.bet = int(input("How much is your bet: "))

        self.player.setBalance(self.player.getBalance() - self.bet)

    def startGame(self):
        self.queryBet();

        print("\n===============================")
        print("=         GAME STARTED        =")
        print("===============================\n")

        self.playerDrewCard()
        self.playerDrewCard()

        self.deck1.drawCard()
        self.deck1.drawCard()
        self.player.hand.displayCard(self.name)

        self.dealerDrewCard()
        self.dealerDrewCard()
        self.dealer.hand.displayCard("Dealer")

        print("Actions:\n[1] Stand\n[2] Hit")
        choice = input("Enter your choice: ")

    def playerDrewCard(self):
        self.player.hand.addCard(self.deck.drawCard())
    
    def dealerDrewCard(self):
        self.dealer.hand.addCard(self.deck.drawCard())
        
# Instantiation of Main Class
main = Main()

# Start the game
main.preparationStage()