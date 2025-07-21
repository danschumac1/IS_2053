'''
2025-07-20
Author: Dan Schumacher
How to run:
   python .\src\lessons\oop\seperate_animals.py
'''

import json

class Cat:
    def __init__(self):
        self.name = "CAT"
        self.type_of_food = "cat_food"
        self.sound = "Meow"

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def favorite_food(self):
        return f"{self.name} eats {self.type_of_food}."

class Dog:
    def __init__(self):
        self.name = "DOG"
        self.type_of_food = "dog_food"
        self.sound = "Woof"

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def favorite_food(self):
        return f"{self.name} eats {self.type_of_food}."

class Cow:
    def __init__(self):
        self.name = "COW"
        self.type_of_food = "grass"
        self.sound = "Moo"

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def favorite_food(self):
        return f"{self.name} eats {self.type_of_food}."


def main():
    cat = Cat()
    dog = Dog()
    cow = Cow()

    cat.speak()
    dog.favorite_food()
    stored_food = (cow.type_of_food)
    print("Cow like to eat: ", stored_food)

if __name__ == "__main__":
    main()
