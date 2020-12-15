"""
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Create at least two objects of each class using the __init__ method.
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

"""


class Airplane:
    def __init__(self, engines, mtow, type):
        self.engines = engines
        self.mtow = mtow
        self.type = type

    def __str__(self):
        return f"This is a {self.engines} engine, {self.type} airplane with a MTOW of {self.mtow}!"

    def __add__(self, other):
        new_engines = self.engines + other.engines
        new_mtow = self.mtow + other.mtow
        return f"We now have {new_engines} engines and {new_mtow} MTOW."


yourPlane = Airplane(1, 1200, "jet")
myPlane = Airplane(2, 4700, "piston")
print(myPlane)
print(yourPlane)
ourPlane = myPlane + yourPlane
print(ourPlane)


class Motorbike:
    def __init__(self, make, color, speed):
        self.make = make
        self.color = color
        self.speed = speed

    def __str__(self):
        return f"This {self.color} {self.make} motorbike has a top speed of {self.speed} km/h!"

    def __add__(self, other):
        new_color = self.color + other.color
        new_speed = self.speed + other.speed
        return f"We now have a {new_color} bike with a top speed of {new_speed} km/h! ;-P"


myBike = Motorbike("Moto Guzzi", "Red", 160)
yourBike = Motorbike("Ducati", "Yellow", 300)
print(myBike, yourBike)
ourBike = myBike + yourBike
print(ourBike)


class Laptop:
    def __init__(self, brand, ram, size):
        self.brand = brand
        self.ram = ram
        self.size = size

    def __str__(self):
        return f"I would like a {self.size} {self.brand} with {self.ram} of RAM please!"


myLaptop = Laptop("mac", "64GB", '15"')
yourLaptop = Laptop("Linux", "32GB", '16"')

print(f"{myLaptop} and {yourLaptop}")
