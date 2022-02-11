# Write your code here :-)
# Write your code here :-)
print("------------- Exercise 9-6 ---------------")
"""An ice cream stand is a specific kind of restaurant. Write a class
called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method."""
class Restaurant ():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " serves " + self.cuisine_type + "."
        print(msg)

    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print(msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served



class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


bardons = IceCreamStand('Bardons')
bardons.flavors = ['vanilla', 'chocolate', 'caramel']

bardons.describe_restaurant()
bardons.show_flavors()
