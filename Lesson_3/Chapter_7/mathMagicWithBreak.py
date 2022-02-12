#mathMagicWithBreak.py
import random
counter = 0
numCorrect = 0
while counter <= 10: #I wasn't sure if you wanted to loop the
#whole thing 10 times, or just have the while loop go ten times, so I just chose one
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
    if counter - numCorrect > 5:
        print('You might want to get some help from a tutor')
    break
print(f'You answered {numCorrect} questions correctly')
print('Thanks for playing') 