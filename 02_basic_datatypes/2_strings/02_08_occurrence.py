'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
string = input("Give me a sentence and I'll count your letters!: ")
letter = input("OK which letter should I count?: ")

print("There's", string.count(letter), letter+"'s in your sentence!")
