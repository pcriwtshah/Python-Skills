class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(self.name.title() +" is an Indian restaurant")
        print(self.cuisine.title() +" is available for $1 only")

    def open_restaurant(self):
        print(self.name.title() + "is open now")

my_restaurant = Restaurant('Sitar', 'Samosa')
print("The restaurant name is " + my_restaurant.name.title())
print("Available cuisine is " + my_restaurant.cuisine.title())

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant_1 = Restaurant('Himalayan', 'Nepalese Cuisine')
my_restaurant_2 = Restaurant('Mantra', 'Tika Masala')
my_restaurant_3 = Restaurant('Bombay House', 'North Indian')

print("The restaurant name is " + my_restaurant_1.name.title())
print("Available cuisine is " + my_restaurant_1.cuisine.title())

my_restaurant_1.describe_restaurant()
my_restaurant_1.open_restaurant()

print("The restaurant name is " + my_restaurant_2.name.title())
print("Available cuisine is " + my_restaurant_2.cuisine.title())

my_restaurant_2.describe_restaurant()
my_restaurant_2.open_restaurant()


print("The restaurant name is " + my_restaurant_3.name.title())
print("Available cuisine is " + my_restaurant_3.cuisine.title())

my_restaurant_3.describe_restaurant()
my_restaurant_3.open_restaurant()