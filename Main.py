from Deck import Deck
from Player import Player

class Main:
    # The function prints a welcome message and creates a deck object.
    def __init__(self):
        print("\n===============================")
        print("=     Welcome to BlackJack    =")
        print("===============================\n")
        self.deck = Deck()
        self.isStand = False

    def preparationStage(self):
        # Asking the user to enter their name.
        self.queryPlayerName()

        # It creates a player object.
        self.createPlayer()

        while(True):
            # Resetting the player's hand and balance.
            self.player.resetAll()

            # Resetting the dealer's hand and balance.
            self.dealer.resetAll()

            # Resetting the deck.
            self.deck.resetDeck()
            self.isStand = False

            # Calling the startGame() function.
            self.startGame()

            # This is the code that asks the user if they want to play again. If the user's balance is
            # 0, then the user cannot play again.
            if(self.player.getBalance() == 0): 
                print("You don't have enough credit balance to play!")
                print("Thank you for playing Black Jack!")
                break
            
            print("Would you like to play again?\n[1] Yes\n[Any] No")
            choice = input("Choice: ")

            print("\n===============================\n")

            if(choice != "1"): break

    # It creates a player and a dealer
    def createPlayer(self):
        self.player = Player(self.name)
        self.dealer = Player("Dealer")

    # This function asks the user to enter their name and then prints a line of equal signs
    def queryPlayerName(self):
        self.name = input("Enter your name: ")
        print("\n===============================\n")
    
    # It asks the user for a bet, and if the bet is greater than the player's balance, it asks the
    # user for a new bet
    def queryBet(self):
        # Asking the user for a bet.
        print("Your credit balance: $" + str(self.player.balance))
        self.bet = int(input("How much is your bet: "))

        # This is a while loop that asks the user for a bet. If the bet is greater than the player's
        # balance, it asks the user for a new bet.
        while(self.bet > self.player.getBalance() or self.bet <= 0):
            print("Insufficient balance! Your remaining balance is " + str(self.player.getBalance()))
            print("\n===============================\n")
            self.bet = int(input("How much is your bet: "))

        # Subtracting the bet from the player's balance.
        self.player.setBalance(self.player.getBalance() - self.bet)

    def startGame(self):
        self.queryBet();
        print("\n===============================")
        print("=         GAME STARTED        =")
        print("===============================\n")

        # Calling the playerDrewTwoCards() and player will drew two cards
        self.playerDrewTwoCards()

        # Calling the playerTurns() and player will make his/her decision.
        self.playerTurns()

        # Calling the dealerTurns() and dealer will draw if his cards < 17.
        self.dealerTurns()

        # Checking the winner of the game.
        self.assessWinner()

        # Displaying the balance of the player.
        self.displayBalance()

    # The player drew two cards, then the dealer drew two cards.
    def playerDrewTwoCards(self):
        # Player will draw two cards
        self.playerDrewCard()
        self.playerDrewCard()

        # Displaying the player's hand card.
        self.player.hand.displayCard()

        # Dealer will draw two cards
        self.dealerDrewCard()
        self.dealerDrewCard()

        # Displaying the dealer's hand card.
        self.dealer.hand.displayCard()

    # The player will draw one card from the deck
    def playerDrewCard(self):
        # Player will draw one card
        self.player.hand.addCard(self.deck.drawCard())
    
    #  The dealer will draw one card from the deck and add it to his hand.
    def dealerDrewCard(self):
        # Dealer will draw one card
        self.dealer.hand.addCard(self.deck.drawCard())
    
    """
    The playerTurns function is a while loop that asks the player to either stand or hit. If the
    player hits, the playerDrewCard function is called and the player's hand card is displayed. If the
    player stands, the isStand variable is set to True
    """
    def playerTurns(self):
        # Checking if the player's hand value is less than 21.
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

    """
    If the player's hand value is less than or equal to 21 and the dealer's hand value is less than
    17, the dealer will draw a card until the dealer's hand value is greater than or equal to 17.

    If the dealer's hand value is greater than or equal to 17 then the card of the dealer will be displayed
    """ 
    def dealerTurns(self):
        if(self.player.hand.getHandValue() <= 21 and self.dealer.hand.getHandValue(self.isStand) < 17): 
            while(self.dealer.hand.getHandValue(self.isStand) < 17):
                self.dealerDrewCard()
                self.dealer.hand.displayCard(self.isStand)
        else:
            self.dealer.hand.displayCard(self.isStand)
    
    """
     If the
    dealer has a score of 21, or if the dealer's score is less than 21 and the player's score is
    greater than 21, or if the dealer's score is less than 21 and the player's score is less than 21
    and the dealer's score is greater than the player's score, the dealer wins. If the player has a
    score of 21, or if the player's score is less than 21 and the dealer's score is greater than 21,
    or if the player's score is less than 21 and the dealer's score is less than 21 and the player's
    score is greater than the dealer's score, the player wins
    """
    def assessWinner(self):
        playerScore = self.player.hand.getHandValue(self.isStand) 
        dealerScore = self.dealer.hand.getHandValue(self.isStand) 

        # If the player's score is greater than 21 and the dealer's score is less than 21, the player loses.
        if(playerScore > 21 and dealerScore < 21):
            print("Game ended. You are BUST!")
        
        # If both the player and the dealer have a score of 21, the game ends in a draw.
        elif(
            (playerScore == 21 and dealerScore == 21) or
            (playerScore == dealerScore)
        ):
            print("Game ended in DRAW!")
        
        # If the dealer has a score of 21, or if the dealer's score is less than 21 and 
        # the player's score is greater than 21, or if the dealer's score is less than 21 
        # and the player's score is less than 21 and the dealer's score is  greater than 
        # the player's score, the dealer wins.
        elif(
            (dealerScore == 21) or
            ((dealerScore < 21 and playerScore > 21) or
            ((dealerScore < 21 and playerScore < 21) and (dealerScore > playerScore)))
        ):
            print("Game ended. Dealer wins!")
        
        # If the player has a score of 21, or if the player's score is less than 21 and
        # the dealer's score is greater than 21, or if the player's score is less than 21
        # and the dealer's score is less than 21 and the player's score is greater than 
        # the dealer's score, the player wins.
        elif(
            (playerScore == 21) or
            (playerScore < 21 and dealerScore > 21) or
            ((playerScore < 21 and dealerScore < 21) and (playerScore > dealerScore))
        ):
            self.player.setBalance((self.bet * 2) + self.player.balance)
            print("Congratulations! You won " + str(self.bet * 2) + ".")

    # This function displays the player's new balance after a bet has been placed
    def displayBalance(self):
        print("\n===============================\n")
        print("Your new credit balance is: $" + str(self.player.getBalance()))
        print("\n===============================\n")

# Instantiation of Main Class
main = Main()

# Start the game
main.preparationStage()