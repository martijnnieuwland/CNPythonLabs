"""
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

"""


def division():
    try:
        num1 = int(input("Give us one number: "))
        num2 = int(input("Give us another number: "))
        print(num1 / num2)
    except ValueError as v:
        print("Come on now! That's not a number!!: ", v)
    except ZeroDivisionError as z:
        print("And how do you expect me to divide by zero?: ", z)
    else:
        print("So there's your answer")
    finally:
        print("Anything else?")


division()
