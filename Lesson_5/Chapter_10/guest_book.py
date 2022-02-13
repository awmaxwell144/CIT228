print('--------------------Exercise 10-3--------------------')
""" Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt."""
"""
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)
"""

print('--------------------Exercise 10-4--------------------')
"""Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file"""
"""
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + "\n")
        print("Hi " + name + ", you've been added to the guest book.")
"""
import random
import os
fileName = 'Lesson_5/Chapter_10/guest_book.txt'
if os.path.exists(fileName):
    os.remove(fileName)
rooms = []
with open(fileName, "w") as guestsFile:
    guest = input('Please enter your name (q for quit)? ')
    while guest != 'q':
        num = random.randint(1,50)
        while num in rooms:
            num = random.randint(1,50)
        print(f'{guest}, you will be in room {num}')
        rooms.append(num)
        guest += ", room number " + str(num) + "\n"
        guestsFile.write(guest)
        guest = input("Please enter your name (q for quit)? ")
with open(fileName) as guestsFile:
    print('------------Guest and Room Assigned------------')
    for line in guestsFile:
        print(line)