'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
numbers = [int(input("I need ten numbers. Give me one then hit enter: "))]
count = len(numbers)

while count < 10:
    numbers.append(int(input(f"{10 - count} more: ")))
    count = len(numbers)
print(numbers)

even = 1
odd = 8
for n in numbers:
    while even < 10:
        print(numbers[even])
        even += 2
    while odd >= 0:
        print(numbers[odd])
        odd -= 2
