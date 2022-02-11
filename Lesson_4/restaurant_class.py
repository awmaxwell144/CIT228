# Write your code here :-)
print("------------- Exercise 9-1 ---------------")
"""Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a
cuisine_type. Make a method called describe_restaurant() that
prints these two pieces of information, and a method called
open_restaurant() that prints a message indi- cating that the
restaurant is open.
Make an instance called restaurant from your class. Print the
two attri- butes individually, and then call both methods."""

class Restaurant ():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + " serves " + self.cuisine_type + " cuisine."
        print(msg)

    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print(msg)

restaurant = Restaurant('TGI Friday', 'American')
print('Restaurant = ' + restaurant.name)
print('Cuisine = ' + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()

print("------------- Exercise 9-2 ---------------")
olive_garden = Restaurant('Olive Garden','Italian')
olive_garden.describe_restaurant()
print()
hunan = Restaurant('Hunan','Chinese')
hunan.describe_restaurant()
print()
la_senorita = Restaurant('La Seniorita','Mexican')
la_senorita.describe_restaurant()
print()
