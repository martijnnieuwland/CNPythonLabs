'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
print(float(7))
print(int(5.92))
print(9.3//2)
x = float(input("Give me the first of two numbers you want to multiply: "))
y = float(input("Good. And the second one?: "))
print("The factor is:", x * y)
