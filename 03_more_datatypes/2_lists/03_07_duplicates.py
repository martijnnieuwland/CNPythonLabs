'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

new_list = []
for n in list_:
    if n not in new_list:
        new_list.append(n)

print(list_)
print(new_list)
