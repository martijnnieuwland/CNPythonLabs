'''
Write a script that takes a tuple and turns it into a list.

'''

sometuple = (1, 6, "word", [89])

somelist = []

for i in sometuple:
    somelist.append(i)
print(type(somelist))
print(somelist)
