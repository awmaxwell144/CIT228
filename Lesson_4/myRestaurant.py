# Write your code here :-)
from restaurant import Restaurant
from icecream import IceCreamStand


print("------------- Exercise 9-1 ---------------")
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

print("------------- Exercise 9-6 ---------------")
bardons = IceCreamStand('Bardons')
bardons.flavors = ['vanilla', 'chocolate', 'caramel']

bardons.describe_restaurant()
bardons.show_flavors()
