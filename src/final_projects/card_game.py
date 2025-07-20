import random
from typing import List, Optional

# === Card Class ===
class Card:
    """Represents a single playing card."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f'{self.rank} of {self.suit}'

# === Deck Class ===
class Deck:
    """Represents a deck of cards."""
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        return self.cards.pop() if self.cards else None

# === Player Class ===
class Player:
    """Represents a player in the game."""
    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.is_ai = is_ai
        self.score = 0

    def play_turn(self, deck: Deck) -> Optional[Card]:
        if deck.cards:
            card = deck.draw_card()
            print(f'{self.name} drew {card}')
            return card
        return None

# === Game Logic ===
def play_game():
    print("Welcome to High Card Wins!")
    player1 = Player(input("Enter name for Player 1: "))
    opponent_type = input("Play against AI? (y/n): ").lower()
    player2 = Player("AI_Bot" if opponent_type == 'y' else input("Enter name for Player 2: "), is_ai=(opponent_type == 'y'))

    deck = Deck()

    while len(deck.cards) >= 2:
        input(f"{player1.name}, press Enter to draw a card.")
        card1 = player1.play_turn(deck)

        if player2.is_ai:
            print(f"{player2.name} (AI) is drawing a card...")
        else:
            input(f"{player2.name}, press Enter to draw a card.")
        card2 = player2.play_turn(deck)

        if card1 and card2:
            winner = compare_cards(card1, card2)
            if winner == 1:
                player1.score += 1
                print(f"{player1.name} wins this round!")
            elif winner == 2:
                player2.score += 1
                print(f"{player2.name} wins this round!")
            else:
                print("This round is a tie!")
        print_scores(player1, player2)

    declare_winner(player1, player2)
    save_results(player1, player2)

    if input("Play again? (y/n): ").lower() == 'y':
        play_game()


def compare_cards(card1: Card, card2: Card) -> int:
    """Compare two cards by rank."""
    rank_order = {rank: index for index, rank in enumerate(Card.ranks)}
    if rank_order[card1.rank] > rank_order[card2.rank]:
        return 1
    elif rank_order[card1.rank] < rank_order[card2.rank]:
        return 2
    return 0

def print_scores(player1: Player, player2: Player):
    print(f"\nScores:\n{player1.name}: {player1.score}\n{player2.name}: {player2.score}\n")

def declare_winner(player1: Player, player2: Player):
    print("\n=== Final Scores ===")
    print_scores(player1, player2)
    if player1.score > player2.score:
        print(f"{player1.name} wins the game!")
    elif player2.score > player1.score:
        print(f"{player2.name} wins the game!")
    else:
        print("The game is a tie!")

def save_results(player1: Player, player2: Player):
    with open('game_results.txt', 'a') as file:
        file.write(f"{player1.name}: {player1.score} | {player2.name}: {player2.score}\n")

if __name__ == "__main__":
    play_game()
