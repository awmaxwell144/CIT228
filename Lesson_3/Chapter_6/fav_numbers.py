#Fav_numbers
""" Use a dictionary to store people’s favorite numbers. Think of
five names, and use them as keys in your dictionary. Think of a
favorite number for each person, and store each as a value in your
dictionary. Print each person’s name and their favorite number.
For even more fun, poll a few friends and get some actual data for
your program."""

favNums = {"Lisa":20, "Dan":22, "Danielle":7,"Dylan":11,"Leighton":13}
for i in favNums:
    print(f'{i}, your favorite animal is: {favNums[i]}')
    