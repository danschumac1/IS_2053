'''
2025-07-20
Author: Dan Schumacher
How to run:
   python .\src\lessons\oop\simplest_oop.py
'''

import json

class Animal:
    def __init__(self, name, type_of_food, sound):
        self.name = name
        self.type_of_food = type_of_food
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def favorite_food(self):
        return f"{self.name} eats {self.type_of_food}."

def main():
    ...

if __name__ == "__main__":
    main()

# Volunteers
cat = Animal("CAT", "cat_food", "Meow")
dog = Animal("DOG", "dog_food", "Woof")
cow = Animal("COW", "grass", "Moo")

animals = [cat, dog, cow]

for animal in animals:
    print(animal.speak())
    print(animal.favorite_food())
