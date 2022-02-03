# Write your code here :-)

#mathMagicWithSentinel.py
import random
keepPlaying = True
numCorrect = 0
while keepPlaying:
    randNum1 = random.randrange(1,1000)
    randNum2 = random.randrange(1,1000)
    correctAns = randNum1 + randNum2
    userAns = int(input(f'What is the value of {randNum1} + {randNum2}? '))
    if (correctAns == userAns):
        print('Good job, your answer was correct!')
        numCorrect += 1
    else:
        print(f'Oops, the correct answer is {correctAns}')
    cont = input('Do you want to keep playing? Yes or No? ').lower()
    if cont == 'no':
        keepPlaying = False
print(f'You answered {numCorrect} questions correctly')
print('Thanks for playing')
