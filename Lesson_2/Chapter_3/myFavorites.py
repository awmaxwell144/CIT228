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