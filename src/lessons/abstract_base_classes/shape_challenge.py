'''
2025-07-21
Lecture Example: Abstract Base Classes in Python
Author: Dan Schumacher
'''

from abc import ABC, abstractmethod
import math

# Define an abstract base class for shapes
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class RightTriangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height =height

    def area(self):
        return .5*(self.width, self.height)
    def perimeter(self):
        c_square = self.width**2 + self.height**2
        c = math.sqrt(c_square)
        return self.width + self.height + c


def main():
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        RightTriangle(3, 4)
    ]

    for shape in shapes:
        print(f"{type(shape).__name__}:")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")
        print("-")


if __name__ == "__main__":
    main()
