#nested dictionaries

people = {1:{"Name":"Bill", "Age" : 46},2:{"Name":"Angela","Age":44}}
for i in people:
    print(f'Person {i}:')
    print(f'\t Name: {people[i]["Name"]}')
    print(f'\t Age: {people[i]["Age"]}')