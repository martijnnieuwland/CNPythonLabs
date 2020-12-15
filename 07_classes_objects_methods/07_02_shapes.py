"""
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

"""
import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        area = self.length * self.width
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.length
        return perimeter


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi*self.radius**2
        return area

    def get_circumference(self):
        circumference = 2*math.pi*self.radius
        return circumference


rectangle = Rectangle(6, 4)
print(f"The rectangle's area is {rectangle.get_area()}, and its perimeter is {rectangle.get_perimeter()}")

circle = Circle(4)
print(f"The circle's area is {circle.get_area()}, and its circumference is {circle.get_circumference()}")
