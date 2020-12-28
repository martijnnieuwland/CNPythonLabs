"""
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

"""

import re

with open("books/war_and_peace.txt", "r") as wp:
    wp_text = wp.read()

with open("books/crime_and_punishment.txt", "w") as cp:
    cp.write("")

books = ["books/war_and_peace.txt", "books/crime_and_punishment.txt", "books/pride_and_prejudice.txt"]


class found_prince(Exception):
    pass
    # print("You have found a Prince")


for book in books:
    try:
        with open(book, "r") as b:
            print(b.readline(1)[0])
    except IndexError as i:
        print("This book has no text!")

for book in books:
    with open(book, "r") as b:
        text = b.read()
        for p in re.finditer("Prince", text[:101]):
            print(book.lstrip("books/").rstrip(".txt"), p.start())  # text.index("Prince", 0, 101))
try:
    if p:
        raise found_prince("You have found a Prince")
except NameError as n:
    print("No Prince found...")
