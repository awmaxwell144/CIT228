print("------------- Exercise 5-7 ---------------")
"""Make a list of your favorite fruits, and then write a
series of independent if statements that check for certain
fruits in your list.
• Make a list of your three favorite fruits and call it
favorite_fruits.
• Write five if statements. Each should check whether a certain
kind of fruit is in your list. If the fruit is in your list, the
if block should print a statement, such as You really like bananas!""" 
favorite_fruits = ["mangoes","bananas","oranges"]
for fruit in favorite_fruits:
    print(f'The fruit is {fruit}')
    if fruit == "mangoes":
        print("Mangoes are delicious")
    elif fruit == "bananas":
        print("Bananas are technically berries")
    else:
        print("There are over 600 varieties of oranges")