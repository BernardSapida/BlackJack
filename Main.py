from Deck import Deck
from Player import Player
from Hand import Hand

class Main:
    def __init__(self):
        print("\n===============================")
        print("=     Welcome to BlackJack    =")
        print("===============================\n")
        self.deck = Deck()
        self.isStand = False

    def preparationStage(self):
        self.queryPlayerName()
        self.createPlayer()

        while(True):
            self.player.resetAll()
            self.dealer.resetAll()
            self.deck.resetDeck()
            self.isStand = False

            self.startGame()

            if(self.player.getBalance() == 0): 
                print("You don't have enough credit balance to play!")
                print("Thank you for playing Black Jack!")
                break
            print("Would you like to play again?\n[1] Yes\n[Any] No")
            choice = input("Choice: ")
            print("\n===============================\n")
            if(choice != "1"): break
                
        
            

    def createPlayer(self):
        self.player = Player(self.name)
        self.dealer = Player("Dealer")

    def queryPlayerName(self):
        self.name = input("Enter your name: ")
        print("\n===============================\n")
    
    def queryBet(self):
        print("Your credit balance: $" + str(self.player.balance))
        self.bet = int(input("How much is your bet: "))

        while(self.bet > self.player.getBalance() or self.bet <= 0):
            print("Insufficient balance! Your remaining balance is " + str(self.player.getBalance()))
            print("\n===============================\n")
            self.bet = int(input("How much is your bet: "))

        self.player.setBalance(self.player.getBalance() - self.bet)

    def startGame(self):
        self.queryBet();
        print("\n===============================")
        print("=         GAME STARTED        =")
        print("===============================\n")

        self.playerDrewTwoCards()
        self.playerTurns()
        self.dealerTurns()
        self.assessWinner()
        self.displayBalance()

    def playerDrewTwoCards(self):
        self.playerDrewCard()
        self.playerDrewCard()
        self.player.hand.displayCard()

        self.dealerDrewCard()
        self.dealerDrewCard()
        self.dealer.hand.displayCard()

    def playerDrewCard(self):
        self.player.hand.addCard(self.deck.drawCard())
    
    def dealerDrewCard(self):
        self.dealer.hand.addCard(self.deck.drawCard())
    
    def playerTurns(self):
        while(self.player.hand.getHandValue() < 21):
            print("Actions:\n[1] Stand\n[2] Hit")
            choice = input("Enter your choice: ")
            print("\n===============================\n")
            if(choice == "1"): break
            if(choice == "2"): 
                self.playerDrewCard()
                self.player.hand.displayCard()
                self.dealer.hand.displayCard()

        self.isStand = True
        
    
    def dealerTurns(self):
        if(self.player.hand.getHandValue() <= 21 and self.dealer.hand.getHandValue(self.isStand) < 17): 
            while(self.dealer.hand.getHandValue(self.isStand) < 17):
                self.dealerDrewCard()
                self.dealer.hand.displayCard(self.isStand)
        else:
            self.dealer.hand.displayCard(self.isStand)
    
    def assessWinner(self):
        playerScore = self.player.hand.getHandValue(self.isStand) 
        dealerScore = self.dealer.hand.getHandValue(self.isStand) 

        if(playerScore > 21 and dealerScore < 21):
            print("Game ended. You are BUST!")
        elif(
            (playerScore == 21 and dealerScore == 21) or
            (playerScore == dealerScore)
        ):
            print("Game ended in DRAW!")
        elif(
            (dealerScore == 21) or
            ((dealerScore < 21 and playerScore > 21) or
            ((dealerScore < 21 and playerScore < 21) and (dealerScore > playerScore)))
        ):
            print("Game ended. Dealer wins!")
        elif(
            (playerScore == 21) or
            (playerScore < 21 and dealerScore > 21) or
            ((playerScore < 21 and dealerScore < 21) and (playerScore > dealerScore))
        ):
            self.player.setBalance((self.bet * 2) + self.player.balance)
            print("Congratulations! You won " + str(self.bet * 2) + ".")
        

    def displayBalance(self):
        print("\n===============================\n")
        print("Your new credit balance is: $" + str(self.player.getBalance()))
        print("\n===============================\n")

# Instantiation of Main Class
main = Main()

# Start the game
main.preparationStage()