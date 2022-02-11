# Write your code here :-)
print("------------- Exercise 9-4 ---------------")
class Restaurant ():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " serves " + self.cuisine_type + " cuisine."
        print(msg)

    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print(msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restaurant('Outback Steakhouse', 'American')
restaurant.describe_restaurant()

print("\nThe starting number of customers: " + str(restaurant.number_served))

restaurant.number_served = 200
print("The number of customers served has been changed to: " + str(restaurant.number_served))

restaurant.set_number_served(300)
print(f'The number served has been changed to {str(restaurant.number_served)} using the set_number_served method')

restaurant.increment_number_served(45)
print("Adding 45 customers to the number served for a total of: " + str(restaurant.number_served))
