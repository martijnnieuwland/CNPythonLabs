'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

num = int(input("Please give me a number between 1 and 1,000,000,000: ").replace(",", ""))

if num % 3 == 0:
    print(f"{num} is divisible by 3.  The quotient is: {num / 3}")
else:
    print(f"{num} is not divisible by 3.  The quotient is: {num // 3} and the remainder is: {num % 3}")
