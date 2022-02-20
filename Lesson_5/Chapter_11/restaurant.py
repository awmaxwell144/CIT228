# Write your code here :-)
class Restaurant ():
    def __init__(self, name, cuisine_type, number_served):
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