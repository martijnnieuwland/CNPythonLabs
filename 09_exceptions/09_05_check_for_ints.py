"""
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

"""

num = "Give me an integer: "

while num is not type(int):
    try:
        num = int(input("Give me an integer: "))
    except ValueError as v:
        print("That's not an integer!")
    else:
        print("Good")
        break
