from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Triangle subclass
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Example usage
if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 8)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")