"""
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

"""

# userAge = int(input("What age are you? "))
#
#
# # Year of birth
#
# def birth_year(userAge):
#     days = days_lived(userAge)
#     return 2020 - (days / 365)
#
#
# # days lived
#
# def days_lived(userAge):
#     yearofbirth = birth_year(userAge)
#     return (2020 - yearofbirth) * 365
#
#
# # Leaps taken
#
# def leaps():
#     years = days_lived(userAge)
#     return years / 4
#
#
# print(birth_year(userAge))
# print(days_lived(userAge))
# print(leaps())


def takeanumber():
    return input("Give me a number ")


def double():
    return takeanumber() * 2


def doubledouble():
    return double() * 2


def doubledoubledouble():
    return doubledouble() * 2



print(double())
print(doubledouble())
print(doubledoubledouble())
