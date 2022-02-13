#glossary
"""A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the
previous chapters. Use these words as the keys in your glossary,
and store their meanings as values.
• Print each word and its meaning as neatly formatted output.
You might print the word followed by a colon and then its meaning,
or print the word on one line and then print its meaning indented
on a second line. Use the newline character (\n) to insert a
blank line between each word-meaning pair in your output."""

glossary = {"Integer":"Whole number",
            "Float":"Decimal number",
            "String":"Text",
            "Boolean":"True/False",
            "List":"A container that can store any kind of values",
            "Tuple":"A similar container as a list that cannot be updated",
            "Index":"A number indicating the location of a specific value within a list of tuple",
            "Comment":"Text within the script that will not be compiled as code",
            "For loop":"A loop that iterates through the contents a set number of times",
            "If statement":"Executes the contents if the statement evaluates to true"
            }

for i in glossary:
    print(i)
    print(f'\t{glossary[i]}')

print('------------For Chapter 10------------')
import pyinputplus as pyip
"""
6.  In the main program, use a while loop to continue processing until the user selects quit from the menu
7.  Make sure your program handles keys that are more than one word  ( For example, if the user enters
 assert method for the term, you will need to format that before you can use it as a key. You could format 
 it as assert_method,  assertMethod or assert-method.)"""
def write_glossary(glossary):
    filename = 'Lesson_5\Chapter_10\glossary.txt'
    with open(filename, 'w') as f: 
        f.write('\n\nWriting to glossary:')
        for item in glossary: 
            f.write(f'\n{item}: {glossary[item]}')

def append_glossary():
    filename = 'Lesson_5\Chapter_10\glossary.txt'
    with open(filename, 'a') as f: 
        while True:
            term = input('Please input a term: ')
            definition = input('Please input the definition: ')
            print(f'\n{term}: {definition}')

def menu():
    while True:
        print('Menu:\n1: Create the glossary json file\n2: Read from the glossary and print the glossary\n3: Add to the glossary json file\n4: Quit')
        choice = int(pyip.inputInt('Please enter a number 1-4: '))
        if choice == 1:
            write_glossary(glossary)
        elif choice == 2:
            with open('Lesson_5\Chapter_10\glossary.txt', 'r') as f: 
                lines = f.readlines()
                for line in lines:
                    print(line)
        elif choice == 3:
            append_glossary()
        elif choice == 4:
            print('Quitting')
            break
        else:
            print('Please enter a valid numerical input between 1 and 4')


menu()
