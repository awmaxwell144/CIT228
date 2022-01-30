# Write your code here :-)


print("-------------Hands on 1---------------")

foods = ["mango","omlette","toast","ice cream","watermelon","coffee"]
print(f'Favorite foods: {foods}')
numbers = [1,2,4,9,12,144]
print(f'Favorite numbers: {numbers}')
movies = ["Hidden Figures","Pirates of the Caribbean","Harry Potter"]
print(f'Favorite movies: {movies}')
combination = foods[:2] + numbers[4:] + movies[:2]
print(f'Combo list: {combination}')
print(f'Last food item: {foods[-1]}')
print(f'2nd, 4th, and 6th numbers: {numbers[1]}, {numbers[3]}, {numbers[5]}')
print(f'All movies: {movies[0]}, {movies[1]}, {movies[2]}')
print(f'First food, number, and movie: {combination[0]}, {combination[2]}, {combination[4]}')

movies.append("Tangled")
print(f'Added movies: {movies}')
numbers.insert(36,3)
print(f'Added number at sub 3: {numbers}')
foods.insert(5,"sandwich")
print(f'Added food at sub 5: {foods}')
del foods[3]
print(f'Deleted food: {foods}')
delLast = numbers.pop()
print(f'Deleted last number: {numbers}')
delTwo = numbers.pop(2)
print(f'Deleted number at sub 2: {numbers}')

movies.sort()
print(f'Sorted movies: {movies}')
foods.sort()
print(f'Sorted foods: {foods}')
print(f'Temp sorted numbers: {sorted(numbers)}')
print(f'Unsorted list: {numbers}')
movies.reverse()
print(f'Sorted in reverse: {movies}')

print("-------------Chapter 4 Hands on 1---------------")
print()
print("Food List")
print("--------------------------------")
for object in foods:
    print(object)
print()
print("Number List")
print("--------------------------------")
for object in numbers:
    print(object)
print()
print("Movie List")
print("--------------------------------")
for object in movies:
    print(object)
print()
print("Combo List")
print("--------------------------------")
for object in combination:
    print(object)






print("-------------Exercise 4-2---------------")
"""Think of at least three different animals that have a common characteristic.
Store the names of these animals in a list, and then use a for loop to print out
the name of each animal.
• Modify your program to print a statement about each animal, such as
A dog would make a great pet.
• Add a line at the end of your program stating what these animals have in common.
You could print a sentence such as Any of these animals would make a great pet!"""

animals = ["Deer", "Fox", "Coyote"]
for animal in animals:
    print(animal)
print("*******Mammals in Northern Michigan*******")
descriptions = [" are herbivores.", " are nocturnal.", " are very good swimmers."]

for i in range(0,3):
    print(animals[i] + descriptions[i])


print("-------------Hands on 3---------------")
animals = ["horse", "cow", "pig", "chicken", "rooster", "goat"]
print("-------------Original List---------------")
for a in animals:
    print(a)
animals2 = animals[0:6]
animals2.append("cat")
animals2.append("dog")
animals2.append("llama")
animals2.append("duck")
print("-------------New List---------------")
for a in animals2:
    print(a)





print("-------------Exercise 4-10---------------")
"""Slices: Using one of the programs you wrote in this chapter,
add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then
use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:.
Use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:.
Use a slice to print the last three items in the list.:"""
print(f'The first 3 items in the new list are: {animals2[0]} {animals2[1]} {animals2[2]}')
print(f'The middle 3 items in the new list are: {animals2[3]} {animals2[4]} {animals2[5]}')
print(f'The last 3 items in the new list are: {animals2[-3]} {animals2[-2]} {animals2[-1]}')


print("-------------Exercise 4-13---------------")
""" Buffet: A buffet-style restaurant offers only five basic foods.
Think of five simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with
different foods. Add a line that rewrites the tuple, and then use a for loop
to print each of the items on the revised menu.
"""
print("******* Buffet Menu *******")
menu = ("eggs","ham","bread","cheese","apples")
for item in menu:
    print(item)
#menu[1] = "bacon"
print("******* New Buffet Menu *******")
menu = ("eggs","bacon","bagels","bread","cheese","apples")
for item in menu:
    print(item)
