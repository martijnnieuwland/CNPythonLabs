"""
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

"""


class Planet:
    def __repr__(self):
        return "Models attributes and methods of a planet object."
    pass


earth = Planet()
print(earth)
