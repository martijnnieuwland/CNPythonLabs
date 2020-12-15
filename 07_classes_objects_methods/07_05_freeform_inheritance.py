'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


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


class Airliner(Airplane):
    def __init__(self, engines, mtow, type, seating):
        super().__init__(engines, mtow, type)
        self.seating = seating

    def __str__(self):
        return f"This is a {self.engines} engine, {self.type} airplane with a MTOW of {self.mtow}" \
               f" and {self.seating} seats."


class Airbus(Airliner):
    def __init__(self, engines, mtow, type, seating, model):
        super().__init__(engines, mtow, type, seating)
        self.model = model

    def __str__(self):
        return f"This is a Airbus {self.model}, {self.engines} engine, {self.type} airplane " \
               f"with a MTOW of {self.mtow} and {self.seating} seats."


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


class Offroadbike(Motorbike):
    def __init__(self, make, color, speed, endurance):
        super().__init__(make, color, speed)
        self.endurance = endurance

    def __str__(self):
        return f"This {self.color} {self.make} motorbike has a top speed of {self.speed} km/h " \
               f"and {self.endurance} hrs of endurance!"


class Laptop:
    def __init__(self, brand, ram, size):
        self.brand = brand
        self.ram = ram
        self.size = size

    def __str__(self):
        return f"I would like a {self.size} {self.brand} with {self.ram} of RAM please!"


myLaptop = Laptop("mac", "64GB", '15"')
yourLaptop = Laptop("Linux", "32GB", '16"')
