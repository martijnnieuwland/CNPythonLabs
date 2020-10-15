'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
import math

# set variables
r = 3.14
pi = math.pi

# calculations
volume = (pi * r**2 * 5)
surface = ((2*pi*r*5)+(2*pi*r**2))

# results
print(volume)
print(surface)
