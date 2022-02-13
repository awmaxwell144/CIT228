print('--------------------Exercise 10-1--------------------')
"""Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads
the file and prints what you wrote three times. Print the contents once by reading 
in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block"""

filename = 'Lesson_5/Chapter_10/learning_python.txt'

print("----------Output from read()----------")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n----------Output from for loop inside with ... open----------")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n----------Output from readlines()----------")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

print('--------------------Exercise 10-2--------------------')
"""Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen"""
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))