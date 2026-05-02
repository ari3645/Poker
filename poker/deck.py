import random
from .card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number=1):
        if number > len(self.cards):
            raise ValueError("Not enough cards in the deck")
        
        dealt_cards = [self.cards.pop() for _ in range(number)]
        return dealt_cards if number > 1 else dealt_cards[0]

    def __len__(self):
        return len(self.cards)
