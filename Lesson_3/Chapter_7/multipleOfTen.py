#multipleofTen.py
"""Ask the user for a number, and then report whether the number
is a multiple of 10 or not."""

num = int(input("Please enter a number: "))
if num % 10 == 0:
    print(f'The number {num} is a multiple of 10')
else:
    print(f'The number {num} is not a multiple of 10')