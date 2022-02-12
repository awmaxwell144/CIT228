#seating.py
"""Write a program that asks the user how many people are in
their dinner group. If the answer is more than eight, print a
message say- ing they’ll have to wait for a table. Otherwise,
report that their table is ready."""
people = int(input("How many people are in your dinner party? "))
if people > 8:
    print("Please wait in the lounge until a table is available.")
else:
    print("Your table is ready.") 