class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def displayCard(self, isStand = False):
        if(self.name == "Dealer"):
            if(isStand == False):
                print(self.name.capitalize() + " Cards: ")
                for card in self.cards:
                    print(card)
                print("\n===============================\n")
            else:
                print(self.name.capitalize() + " Cards: ")
                for index in range(0, len(self.cards)):
                    if(index == len(self.cards) - 1):
                        print("Unknown Card (Hidden)")
                    else:
                        print(self.cards[index])
                print("\n===============================\n")
        else:
            print(self.name.capitalize() + " Cards: ")
            for card in self.cards:
                print(card)
            print("\n===============================\n")
    
    def displayHandValue(self):
        