#rivers
"""Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile
runs through Egypt.
• Use a loop to print the name of each river included in the
dictionary.
• Use a loop to print the name of each country included in the
dictionary.
"""
riversCountries = {"Nile":['Egypt','Tanzania','Rwanda','Kenya'],"Mississippi":"United States","Amazon":['Brazil','Bolivia','Peru','Ecuador']}
print('Rivers & Countries')
for i in riversCountries:
    print(f'The {i} river flows through {riversCountries[i]}')
print()

print('Rivers')
for i in riversCountries:
    print(i)
print()

print('Countries')
for i in riversCountries:
    print(riversCountries[i])
print()