'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

result = {}

for (k, v), (k2, v2) in zip(dict_1.items(), dict_2.items()):
    for k in list(dict_1.keys()):
        if k == k2:
            result[k] = dict_1[k] + dict_2[k2]
        elif k not in list(dict_2.keys()):
            result[k] = dict_1[k]
        elif k2 not in list(dict_1.keys()):
            result[k2] = dict_2[k2]

print(f"final result is: {result}")
