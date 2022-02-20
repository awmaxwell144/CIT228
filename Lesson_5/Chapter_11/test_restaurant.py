# Write your code here :-)
import unittest
from restaurant import Restaurant
class TestRestaurant(unittest.TestCase):
    def setUp(self):
        name = "Betty's Restaurant"
        cuisine_type = "American"
        number_served = 100
        self.restaurant = Restaurant(name, cuisine_type, number_served)


    def test_set_number_served_int(self):
        num_served = 150
        self.restaurant.set_number_served(num_served)
        self.assertEqual(self.restaurant.set_number_served(num_served), 150)

    def test_set_number_served_string(self):
        num_served="150"
        self.restaurant.set_number_served(num_served)
        self.assertEqual(self.restaurant.number_served,150)

    def test_increment_number_served_float(self):
        restaurant=120.50
        self.Restaurant.increment_number_served(restaurant)
        self.assertEqual(self.Restaurant.number_served,220.50)

    def test_increment_number_served_string(self):
        restaurant="120"
        self.Restaurant.increment_number_served(restaurant)
        self.assertEqual(self.Restaurant.daily_number_served,220)

if __name__ == '__main__':
    unittest.main()
