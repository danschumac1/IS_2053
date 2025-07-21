'''
2025-07-21
Author: Dan Schumacher
How to run:
   python .\src\lessons\get_best_out_of_ai\gpt_returned.py
'''

import random
from abc import ABC, abstractmethod
import os

class Creature(ABC):
    def __init__(self, name: str, health: int, attack_range: tuple, ability_points: int, attack_sounds: list):
        self.name = name
        self.health = health
        self.attack_range = attack_range
        self.ability_points = ability_points
        self.attack_sounds = attack_sounds
        self.alive = True

    def attack(self, creature: 'Creature'):
        damage = random.randint(*self.attack_range)
        sound = random.choice(self.attack_sounds)
        print(f"{self.name} attacks with {sound} for {damage} damage!")
        creature.damage(damage)

    def damage(self, damage: int):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")
        if self.health <= 0:
            self.alive = False
            print(f"{self.name} has been defeated!")

    @abstractmethod
    def special_attack(self, creature: 'Creature'):
        pass

class Player(Creature):
    def __init__(self, name):
        super().__init__(name, health=30, attack_range=(3, 7), ability_points=3, attack_sounds=['Slash', 'Stab'])

    def special_attack(self, creature: 'Creature'):
        if self.ability_points > 0:
            self.ability_points -= 1
            heal_amount = random.randint(5, 10)
            self.health += heal_amount
            print(f"{self.name} uses special ability to heal {heal_amount} health! Health is now {self.health}.")
        else:
            print("No ability points left!")

class Enemy(Creature):
    def __init__(self, name):
        super().__init__(name, health=25, attack_range=(2, 5), ability_points=2, attack_sounds=['Roar', 'Smash'])
        self.miss_next = 0

    def special_attack(self, creature: 'Creature'):
        if self.ability_points > 0:
            self.ability_points -= 1
            if random.choice([True, False]):
                creature.miss_next = 1
                print(f"{self.name} uses a special attack! {creature.name} will miss their next turn!")
            else:
                print(f"{self.name} tried a special attack, but it failed!")
        else:
            print(f"{self.name} has no ability points left!")

class CombatWindow:
    def __init__(self):
        pass

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_stats(self, player: Player, enemy: Enemy):
        print("\n=== Battle Status ===")
        print(f"{player.name}: {player.health} HP, Ability Points: {player.ability_points}")
        print(f"{enemy.name}: {enemy.health} HP, Ability Points: {enemy.ability_points}")


def play_game():
    player = Player('Hero')
    enemy = Enemy('Goblin')
    ui = CombatWindow()

    player.miss_next = 0

    while player.alive and enemy.alive:
        ui.clear_screen()
        ui.show_stats(player, enemy)

        if player.miss_next:
            print(f"{player.name} misses this turn!")
            player.miss_next = 0
        else:
            action = input("Choose your action: ATTACK or SPECIAL? ").strip().lower()
            if action == 'attack':
                player.attack(enemy)
            elif action == 'special':
                player.special_attack(enemy)
            else:
                print("Invalid action.")
                continue

        if enemy.alive:
            if random.random() < 0.25:
                enemy.special_attack(player)
            else:
                enemy.attack(player)

        input("Press Enter to continue...")

    if player.alive:
        print("\nVictory! You have defeated the enemy!")
    else:
        print("\nDefeat... The enemy was too strong.")


def main():
    play_game()


if __name__ == "__main__":
    main()
