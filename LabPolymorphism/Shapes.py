import math
from abc import ABC ,abstractmethod
class Shape:
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,calculate):
        self.calculate = calculate
    def calculate_area(self):
        return math.pi * self.calculate **2
    def calculate_perimeter(self):
        return 2*math.pi*self.calculate

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length*self.width
    def calculate_perimeter(self):
        return 2*(self.width + self.length)
    

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
78.53981633974483
31.41592653589793
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())