'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

string = input("Hey, give me a string: ")
words = string.split(" ")
max_occurrence = 0

# print(words)

for word in words:
    occurrence = words.count(word)
    if occurrence > max_occurrence:
        max_occurrence = occurrence

max_word = []
for word in words:
    if words.count(word) == max_occurrence and word not in max_word:
        max_word.append(word)
print(f"The word '{', '.join(max_word[0:-1])}' and '{max_word[-1]}' occurred {max_occurrence} times.")

# print(max_word)
