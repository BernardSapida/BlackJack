class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.handValue = 0

    def addCard(self, card):
        self.cards.append(card)

    def displayCard(self, isStand = False):
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
        else:
            print(self.name.capitalize() + " Cards: ")
            for card in self.cards:
                print(card)
            print("Total Card Value: " + str(self.getHandValue()))
            print("\n===============================\n")
    
    def getHandValue(self, isStand = False):
        numberOfAce = 0

        if(self.name == "Dealer"):
            self.handValue = 0

            if(isStand == False):
                for index in range(0, len(self.cards) - 1):
                    cardValue = self.cards[index].split(" ")[0]
                    if(cardValue == "Ace"): 
                        self.handValue += 1
                        numberOfAce += 1
                    elif(cardValue == "Queen" or cardValue == "King" or cardValue == "Jack"): self.handValue += 10
                    else: self.handValue += int(cardValue)
            else:
                for index in range(0, len(self.cards)):
                    cardValue = self.cards[index].split(" ")[0]
                    if(cardValue == "Ace"): 
                        self.handValue += 1
                        numberOfAce += 1
                    elif(cardValue == "Queen" or cardValue == "King" or cardValue == "Jack"): self.handValue += 10
                    else: self.handValue += int(cardValue)
            return self.handValue + 10 if (numberOfAce >= 1 and (self.handValue + 10 == 21)) else self.handValue;
        else:
            self.handValue = 0
            for card in self.cards:
                cardValue = card.split(" ")[0]
                if(cardValue == "Ace"): 
                    self.handValue += 1
                    numberOfAce += 1
                elif(cardValue == "Queen" or cardValue == "King" or cardValue == "Jack"): self.handValue += 10
                else: self.handValue += int(cardValue)
            return self.handValue + 10 if (numberOfAce >= 1 and (self.handValue + 10 == 21)) else self.handValue;