"""

Write a script that completes the following tasks.

"""


# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean


def bool47(number):
    return bool(number % 4 == 0 or number % 7 == 0)
    # return either


# print(bool47(40))

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean


def both47(number):
    return bool(number % 4 == 0 and number % 7 == 0)
    # return both


# print(both47(741))

# take in a number from the user between 1 and 1,000,000,000

inputNumber = int(input('Give me a number between 1 and 1,000,000,000: '))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

either = bool47(inputNumber)

both = both47(inputNumber)

# print your new variables to display the results

print(either)
print(both)
