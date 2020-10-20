'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

number = int(input("Hi give me a number: "))

if isinstance(number, int):
    if number in range(1, (len(months) + 1)):
        print(months[number - 1])
    else:
        print("Other")
