'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]


def stats(inputList):
    print(max(inputList))
    print(min(inputList))
    print(sum(inputList)/len(inputList))
    print(sum(inputList))
    # define the function here
    pass


# call the function below here
stats(example_list)
