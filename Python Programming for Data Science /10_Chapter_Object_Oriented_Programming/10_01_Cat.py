'''A class is a set of instructions to create an instance'''
class Cat(): # Define a class called Dog; Class name starts with capital letters
    """A simple attempt to model a dog.""" #All functions inside class are methods
    def __init__(self, name, age): #runs automatically when we create a new instance using Dog class; Python's default method to name __xxxx__
        """Initialize name and age attributes."""
        '''self is passed automatically, so we don’t need to pass it'''
        self.name = name  #name and age are an attribute
        '''self.name = name takes the value stored in the parameter name (parameter passed through class Dog) 
        and stores it in the variable name, which is then attached to the instance being created.'''
        self.age = age
    '''Any functions defined below are methods of a class'''
    def sit(self):
        """Simulate a dog sitting in response to a command.""" 
        print(self.name.title() + " is now sitting.")
       
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_cat = Cat('willie', 6) #Creating an instance from class Dog
'''my_dog is an instance (all small letters) and Dog is a class (starts with capital letters)'''
print("My dog's name is " + my_cat.name.title() + ".") #title() is used here to capitalize the first letter of a name
print("My dog is " + str(my_cat.age) + " years old.")

my_cat.sit() #Use dot notation to call any methods from class Dog
my_cat.roll_over() ##Use dot notation to call any methods from class Dog
