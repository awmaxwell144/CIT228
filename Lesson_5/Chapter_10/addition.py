print('--------------------Exercise 10-6--------------------')
""": One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a TypeError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number."""
try:
    x = input("Please enter the first number: ")
    x = int(x)

    y = input("Please enter the second numbr: ")
    y = int(y)

except ValueError:
    print("You must enter numbers instead of text, please try again.")

else:
    sum = x + y
    print( str(x) + " + " + str(y) + " = " + str(sum))

print('--------------------Exercise 10-7--------------------')
"""Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number"""
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nPlease enter the first number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Please enter the second number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("You must enter numbers instead of text, please try again.")

    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")