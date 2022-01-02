class Vehicle():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year): 
        """Initialize attributes to describe a car.""" 
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

my_car_1 = Vehicle('toyota', 'camry', 2021) 
print(my_car_1.get_descriptive_name())