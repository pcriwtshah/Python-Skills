class Dog(): # Define a class called Dog; Class name starts with capital letters
    """A simple attempt to model a dog.""" #All functions inside class are methods
def __init__(self, name, age): #runs automatically when we create a new instance using Dog class; Python's default method names __xxxx__
    """Initialize name and age attributes."""
    self.name = name 
    self.age = age
def sit(self):
    """Simulate a dog sitting in response to a command.""" 
    print(self.name.title() + " is now sitting.")
       
def roll_over(self):
    """Simulate rolling over in response to a command."""
    print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")