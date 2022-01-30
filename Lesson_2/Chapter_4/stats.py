import random

number = random.randrange(10,100)
numList = list(range(number))
print(numList)
print(f'The largest number = {max(numList)}')
print(f'The smallest number = {min(numList)}')
print(f'The total of all the = {sum(numList)}')
print(f'The average number = {(sum(numList))/(len(numList))}')
