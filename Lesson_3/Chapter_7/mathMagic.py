
#mathMagic.py
import random
problems = int(input("How many problems would you like to practice? "))
counter = 0
numCorrect = 0
while counter < problems: 
    randNum1 = random.randrange(1,1000)
    randNum2 = random.randrange(1,1000)
    correctAns = randNum1 + randNum2
    userAns = int(input(f'What is the value of {randNum1} + {randNum2}? '))
    if (correctAns == userAns):
        print('Good job, your answer was correct!')
        numCorrect += 1
 
    else:
        print(f'Oops, the correct answer is {correctAns}')
    counter += 1
print(f'You answered {numCorrect} questions correctly')
print('Thanks for playing')