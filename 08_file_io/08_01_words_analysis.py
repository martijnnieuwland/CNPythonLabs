'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

with open("words.txt", "r") as w:
    w_list = []
    for word in w:
        w_list.append(word.strip("\n"))

short = len(min(w_list, key=len))
for word in w_list:
    if len(word) != short:
        continue
    print(word)

long = len(max(w_list, key=len))
for word in w_list:
    if len(word) != long:
        continue
    print(word)

print(len(w_list))
