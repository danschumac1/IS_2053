'''
2025-07-20
Author: Dan Schumacher
Example of Object-Oriented Programming (OOP) with a Deck of Cards
How to run:
    python .\src\lessons\oop\deck_of_cards.py
'''

import random

class Card:
    """Represents a single playing card."""
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """Represents a deck of 52 playing cards."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        """Shuffles the deck in place."""
        random.shuffle(self.cards)

    def deal_card(self):
        """Deals a card from the deck. Returns None if the deck is empty."""
        if len(self.cards) > 0:
            return self.cards.pop()
        return None

    def __len__(self):
        return len(self.cards)


class Player:
    """Represents a player in a card game."""
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def draw(self, deck: Deck, num_cards: int = 1):
        for _ in range(num_cards):
            card = deck.deal_card()
            if card:
                self.hand.append(card)

    def show_hand(self):
        return f"{self.name}'s hand: {[str(card) for card in self.hand]}"


# Example usage:
def main():
    deck = Deck()
    deck.shuffle()

    player1 = Player("Alice")
    player2 = Player("Bob")

    player1.draw(deck, 5)
    player2.draw(deck, 5)

    print(player1.show_hand())
    print(player2.show_hand())
    print(f"Cards remaining in deck: {len(deck)}")


if __name__ == "__main__":
    main()
