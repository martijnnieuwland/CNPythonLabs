'''
Print out every prime number between 1 and 100.

'''

for i in range(1, 101):
    for num in range(2, i):
        if (i % num) == 0:
            break
    else:
        print(i)
