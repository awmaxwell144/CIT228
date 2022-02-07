# Write your code here :-)

print("-------------Hands on 1---------------")
"""
5-1 Write a series of conditional tests. Print a statement describing
each test and your prediction for the results of each test. Your code should
look something like this:
    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False.

5-2 Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality,
  greater than and less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""
color = "Orange"
num1 = 10 
num2 = 20
breakfast = ["pancakes","waffles","eggs","bacon"]

print("============== True Results ==============")
print(f'{num1} < {num2} {num1 < num2}')
print(f'{num1} <= {num2} {num1 <= num2}')
print(f'{num1} != {num2} {num1 != num2}')
print(f'{color} == Orange {color == "Orange"}')
print(f'{color.lower()} == Orange {color.lower() == "orange"}')
print(f'Pancakes in breakfast list? {"pancakes" in breakfast}')
print(f'num1 == 10 and num2 == 20? {num1 == 10 and num2 == 20}')
print(f'num1 == 10 or num2 1= 10? {num1 == 10 or num2 != 10}')

print("============== False Results ==============")
print(f'{num1} > {num2} {num1 > num2}')
print(f'{num1} >= {num2} {num1 >= num2}')
print(f'{num1} == {num2} {num1 == num2}')
print(f'{color} != Orange {color != "Orange"}')
print(f'{color.lower()} == ORANGE {color.lower() == "ORANGE"}')
print(f'Bagels in breakfast list? {"bagels" in breakfast}')