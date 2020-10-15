'''

Write a script that takes in a number in days from the user between 1 and 1,000,000,000 and convert it to seconds.

NOTE: We will use the input() funtion to collect users input. An example is demonstrated below.

'''

# the input of the user will be saved in the variable days.
# because the input() function collects the input as a string, we have to convert it to an int
# The string passed to the input() function is what the user is prompted with
days = int(input("Please enter a number in days between 1 and 1,000,000,000: "))
seconds = days * 24 * 60 * 60

if 0 < days < 1000000000:
    print("That is equal to", seconds, "seconds")
else:
    print("The number in days must be between 1 and 1,000,000,000!")
