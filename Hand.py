class Hand:
    """
    The function __init__() is a constructor that initializes the name and cards attributes of the
    Player class
    
    :param name: The name of the player
    """
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.handValue = 0

    """
    The function addCard takes in a card object and adds it to the list of cards in the deck
    
    :param card: The card to add to the hand
    """
    def addCard(self, card):
        self.cards.append(card)

    def displayCard(self, isStand = False):
        # Checking if the name of the player is "Dealer" and if it is, it will check if the player is
        # standing. If the player is standing, it will print the cards in the hand and the total value
        # of the hand. If the player is not standing, it will print the cards in the hand and the
        # total value of the hand, but it will hide the last card.
        if(self.name == "Dealer"):
            if(isStand == True):
                print(self.name.capitalize() + " Cards: ")
                for card in self.cards:
                    print(card)
                print("Total Card Value: " + str(self.getHandValue(True)))
                print("\n===============================\n")
            else:
                print(self.name.capitalize() + " Cards: ")
                for index in range(0, len(self.cards)):
                    if(index == len(self.cards) - 1):
                        print("Unknown Card (Hidden)")
                    else:
                        print(self.cards[index])
                print("Total Card Value: " + str(self.getHandValue()))
                print("\n===============================\n")
        
        # If the name of the player isn't "Dealer" then it will print all cards and 
        # the total value of the player.
        else:
            print(self.name.capitalize() + " Cards: ")
            for card in self.cards: print(card)
            print("Total Card Value: " + str(self.getHandValue()))
            print("\n===============================\n")
    
    def getHandValue(self, isStand = False):
        numberOfAce = 0

        # Checking if the name of the player is "Dealer"
        if(self.name == "Dealer"):
            self.handValue = 0

            # Checking if the player is standing. If the player is standing, it will print the cards
            # in the hand and the total value of the hand. If the player is not standing, it will
            # print the cards in the hand and the total value of the hand, but it will hide the last
            # card.
            if(isStand == False):
                for index in range(0, len(self.cards) - 1):
                    # Splitting the card value and the suit of the card.
                    cardValue = self.cards[index].split(" ")[0]

                    # This is checking if the card is an Ace. If it is, it will add 1 to the handValue and numberOfAce.
                    if(cardValue == "Ace"): 
                        self.handValue += 1
                        numberOfAce += 1

                    # Checking if the card is a Queen, King, or Jack. If it is, it will add 10 to the handValue.
                    elif(cardValue == "Queen" or cardValue == "King" or cardValue == "Jack"): self.handValue += 10
                    
                    # Else the card isnt a Ace, Queen, King, or Jack. it will add number of the card to the handValue.
                    else: self.handValue += int(cardValue)

            else:
                for index in range(0, len(self.cards)):
                    # Splitting the card value and the suit of the card.
                    cardValue = self.cards[index].split(" ")[0]

                    # This is checking if the card is an Ace. If it is, it will add 1 to the handValue  and numberOfAce.
                    if(cardValue == "Ace"): 
                        self.handValue += 1
                        numberOfAce += 1

                    # Checking if the card is a Queen, King, or Jack. If it is, it will add 10 to the handValue.
                    elif(cardValue == "Queen" or cardValue == "King" or cardValue == "Jack"): self.handValue += 10
                    
                    # Else the card isnt a Ace, Queen, King, or Jack. it will add number of the card to the handValue.
                    else: self.handValue += int(cardValue)

            # Checking if the player has an Ace and if the player has an Ace, it will check if the
            # player has a total value of 21. If the player has a total value of 21, it will add 10 to
            # the handValue.
            return self.handValue + 10 if (numberOfAce >= 1 and (self.handValue + 10 == 21)) else self.handValue;
        else:
            self.handValue = 0
            
            for card in self.cards:
                # Splitting the card value and the suit of the card.
                cardValue = card.split(" ")[0]

                # This is checking if the card is an Ace. If it is, it will add 1 to the handValue  and numberOfAce.
                if(cardValue == "Ace"): 
                    self.handValue += 1
                    numberOfAce += 1

                # Checking if the card is a Queen, King, or Jack. If it is, it will add 10 to the handValue.
                elif(cardValue == "Queen" or cardValue == "King" or cardValue == "Jack"): self.handValue += 10
                
                # Else the card isnt a Ace, Queen, King, or Jack. it will add number of the card to the handValue.
                else: self.handValue += int(cardValue)

            # Checking if the player has an Ace and if the player has an Ace, it will check if the
            # player has a total value of 21. If the player has a total value of 21, it will add 10 to
            # the handValue.
            return self.handValue + 10 if (numberOfAce >= 1 and (self.handValue + 10 == 21)) else self.handValue;