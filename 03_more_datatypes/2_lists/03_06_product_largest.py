'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

numbers = [int(input("I need ten numbers. Give me one then hit enter: "))]
count = len(numbers)

while count < 10:
    numbers.append(int(input(f"{10 - count} more: ")))
    count = len(numbers)
# print(numbers)

print(f"The largest number you gave me was {max(numbers)}.")

product = 1
for n in numbers:
    product = n * product
print(f"The product of all your numbers is {product}.")
