print("-------------Hands on 1---------------")

foods = ["mango","omlette","toast","ice cream"," watermelon","coffee"]
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

print("-------------Hands on 2-------------")
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

print("-------------Hands on 3-------------")
movies.sort()
print(f'Sorted movies: {movies}')
foods.sort()
print(f'Sorted foods: {foods}')
print(f'Temp sorted numbers: {sorted(numbers)}')
print(f'Unsorted list: {numbers}')
movies.reverse()
print(f'Sorted in reverse: {movies}')

#file_guests.py

print("-------------Exercise 3-4-------------")
"""Guest List: If you could invite anyone, living
or deceased, to dinner, who would you invite? Make a
list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message
to each person, inviting them to dinner."""
guests = ["Mom", "Dad", "Robert Frost"]
invitation = ", can you come to dinner next Friday?"
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print()

print("-------------Exercise 3-5-------------")
"""You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
"""
unavailable = guests.pop(2)
guests.append("Ada Lovelace")
print(f'{unavailable} is not able to make it to dinner')
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print()

print("-------------Exercise 3-6-------------")
"""You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5.
    Add a print() call to the end of your program informing people that you found a bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list."""

print("I found a bigger dinner table")
guests.insert(0,"Grandma")
guests.insert(2,"Opa")
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print(guests[3] + invitation)
print(guests[4] + invitation)
print(f'I am inviting {len(guests)} guests to dinner')
print()

print("-------------Exercise 3-7-------------")
"""You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line
that prints a message saying that you can invite only two
people for dinner.
• Use pop() to remove guests from your list one at a
time until only two names remain in your list. Each
time you pop a name from your list, print a message
to that person letting them know you’re sorry you can’t
invite them to dinner.
• Print a message to each of the two people still on
your list, letting them know they’re still invited.
• Use del to remove the last two names from your list,
so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program."""

print("My new dinner table wont arrive in time and I can only invite 2 people")
insert = guests.pop(0)
noSpace = []
noSpace.append(insert)
insert = guests.pop(1)
noSpace.append(insert)
insert = guests.pop(2)
noSpace.append(insert)
apology = ", sorry, I cannot have you over for dinner"
print(noSpace[0] + apology)
print(noSpace[1] + apology)
print(noSpace[2] + apology)
print(guests[0] + invitation)
print(guests[1] + invitation)
del guests[0]
del guests[0]
print(f'Here\'s my revised list: {guests}')
print()

print("-------------Exercise 3-10-------------")
""" Think of something you could store in a list.
For example, you could make a list of mountains, rivers,
countries, cities, languages, or any- thing else you’d like.
Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once."""
print("Trees")
print()
trees = ['Pine','Oak','Birch','Maple', 'Redwood']
print(f'Original List: {trees}')
trees.append('Willow')
print(f'Appended List: {trees}')
trees.insert(2,'Beech')
print(f'With Inserted Item: {trees}')
del trees[5]
deleted = trees.pop(1)
print(f'List With Deletions {trees}')
print(f'Temporary Sort: {sorted(trees)}')
trees.reverse()
print(f'Reverse Sort: {trees}')
trees.sort()
print(f'Alphabetical Sort: {trees}')
print(f'There are {len(trees)} items on the final list')

