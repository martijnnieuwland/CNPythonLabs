"""
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

"""

integer = 'integers.txt'

try:
    with open("integers.txt", "r") as i:
        data = i.readlines()
        num = data[0].rstrip("\n")
        print(int(num) * 100)
except IOError as i:
    print("This file does not exist: ", i)
except ValueError as v:
    print("This was not a number: ", v)
