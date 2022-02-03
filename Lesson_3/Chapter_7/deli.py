#deli.py 
""""
Make a list called sandwich_orders and fill it with the names
of vari- ous sandwiches. Then make an empty list called
finished_sandwiches. Loop through the list of sandwich orders
and print a message for each order, such as I made your tuna sandwich.
As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each
sandwich that was made."""
orders = ['Vegan', 'Pastrami', 'Italian', 'Pastrami', 'Steak', 'Pastrami']
finished = []
print("I'm sorry, we're all out of Pastrami today.")
while 'Pastrami' in orders:
    orders.remove('Pastrami')

while orders:
    current_sandwich = orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished.append(current_sandwich)

print()
print('Sandwiches that were made today include:')
for sandwich in finished:
    print(sandwich)