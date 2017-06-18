#deck.py
import random
    
class deck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    """
    Construct the 52-card deck
    """
    def __init__(self):
        self.cards = []
        for suit in deck.suits:
            for val in deck.values:
                self.cards.append("{} of {}".format(val, suit))

    """
    Deal one card then remove that card from the deck
    """
    def deal_one(self):
        self.cards.pop()

    """
    Give the cards in the deck a random order
    """
    def shuffle(self):
        random.shuffle(self.cards)

    """
    Deal all of the cards and remove them all from the deck
    """
    def deal_all(self):
        for index in range(0, len(self.cards)):
            self.deal_one()

            
