'''
2025-07-21
Lecture Example: Abstract Base Classes in Python
Author: Dan Schumacher
'''

from abc import ABC, abstractmethod

# Define an abstract base class for calculations
class Calculator(ABC):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def calculate(self):
        pass

    def print_nums(self):
        print(f"My numbers are {self.a} and {self.b}")


# Concrete subclass for addition
class Adder(Calculator):
    def calculate(self):
        return self.a + self.b


# Concrete subclass for multiplication
class Multiplier(Calculator):
    def calculate(self):
        return self.a * self.b


# Concrete subclass for exponentiation
class Power(Calculator):
    def calculate(self):
        return self.a ** self.b


# Demonstrating polymorphism via a for loop
def main():
    number1 = 3
    number2 = 4

    calculators = [
        Adder(number1, number2),
        Multiplier(number1, number2),
        Power(number1, number2)
    ]

    results = []
    for calc in calculators:
        result = calc.calculate()
        results.append(result)

    print("Results:", results)
    # Output: [7, 12, 81]


if __name__ == "__main__":
    main()
