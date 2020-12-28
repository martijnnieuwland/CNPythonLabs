"""
Write a script that demonstrates a try/except/else.

"""


class UnexpectedError(Exception):
    pass
    # print("No 0.1 times 3 is not equal to 0.3!")


try:
    if 0.3 == 0.1 * 3:
        print("Yes it is")
except NameError as t:
    raise UnexpectedError("No 0.1 times 3 is not equal to 0.3!")
else:
    print("Anybody knows 0.1 times 3 equals 0.3!")
finally:
    print("What a stupid question!")
