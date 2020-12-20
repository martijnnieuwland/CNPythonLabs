'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

w_list = []
with open("words.txt", "r") as w:
    for word in w.readlines():
        word = word.rstrip()
        w_list.append(word)

with open("words_reverse.txt", "w") as n:
    n.write("\n".join(reversed(w_list)))
