'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

# for n in range(1, 1001):
#     while n % 5 == 0:
#         print(n)
#         pass

n = 0
while 0 <= n <= 1000:
    n += 1
    if n % 5 == 0:
        print(n)
