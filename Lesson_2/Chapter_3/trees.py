
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

