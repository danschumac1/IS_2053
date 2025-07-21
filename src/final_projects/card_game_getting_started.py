import random

# === Card Class ===
class Card:
    """Represents a single playing card with a rank and suit."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f'{self.rank} of {self.suit}'

# === Deck Class ===
class Deck:
    """Represents a shuffled deck of 52 playing cards."""
    def __init__(self):
        # Create all combinations of ranks and suits
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    def draw_card(self):
        """Draw a card from the deck. Returns None if the deck is empty."""
        return self.cards.pop() if self.cards else None


def main():
    deck = Deck()
    print("Drawing 5 cards from the deck:")

    for _ in range(5):
        card = deck.draw_card()
        if card:
            print(f'Drew: {card}')
        else:
            print('No more cards to draw!')


# === Example Usage ===
if __name__ == "__main__":
    main()