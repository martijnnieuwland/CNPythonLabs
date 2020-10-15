'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
string = input("Let me count your vowels!: ").lower()
a = string.count("a")
e = string.count("e")
i = string.count("i")
o = string.count("o")
u = string.count("u")
vowels = a + e + i + o + u

print("There are", vowels, "vowels in your sentence")
print(a, "x an a\n" + str(e), "x an e\n" + str(i), "x an i\n" + str(o), "x an o\n" + str(u), "x a u")
