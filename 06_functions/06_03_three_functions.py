"""
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

"""


def take_a_number():
    return input("Give me a number ")


def double():
    return take_a_number() * 2


def double_double():
    return double() * 2


def double_double_double():
    return double_double() * 2


print(double())
print(double_double())
print(double_double_double())
