'''
2025-07-21
Author: Dan Schumacher
How to run:
   python .\src\lessons\get_best_out_of_ai\turn_based_combat.py
'''

import json

class Creature(ABC):
    def init
    name
    health
    attack_range : tuple
    ability_points: 
    attack_sounds [...]
    alive = True

    def attack(self, creature:Creature)
        creature.damage(
            rand(attack_range)
        )
    def damage(self, damage:int)
        self.health -= damage
         
    @abstractmethod
    def special_attack()
        pass

class Player(Creature)
    def init
    super
    def special_attack():
        '''heals player'''

class Enemy(Creauture)
    def init
    super
    miss_next = 0
    def special_attack()
        '''50/50 Plyaer chance misses next shot'''
        ...

class CombatWindow()
    def __init__(self):
        ...
    clear screen

    show stats(Enemy, Player)

def play_game():
    while enemy or creature alive:
        player.take_turn
        enemy.take_turn

    print(victory condidtions)
def main():
    player = Player(blah)
    enemy = Enemy(blah)

if __name__ == "__main__":
    main()