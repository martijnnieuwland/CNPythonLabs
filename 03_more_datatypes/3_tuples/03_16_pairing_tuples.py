"""
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

"""
numbers = [input("Give me a list of comma separated numbers please: ")]
split_numbers = numbers[0].split(",")

int_numbers = []
for number in split_numbers:
    int_numbers.append(int(number))

sorted_numbers = sorted(int_numbers)
print(f"sorted_numbers: {sorted_numbers}")

tupled_numbers = []
run = len(sorted_numbers)
x = 0
for number in sorted_numbers:
    if run >= 2:
        tupled_numbers.append((sorted_numbers[x], sorted_numbers[x + 1]))
        run -= 2
        x += 2
    elif run == 1:
        tupled_numbers.append((sorted_numbers[x], 0))
        run -= 1

for t in tupled_numbers:
    print(t)
