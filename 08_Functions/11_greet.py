'''
def greet(name):
    print("Good Day " + name)

greet("Harry")
'''
def greet(name = "Stranger"): #Default parameter value
    print("Good Day " + name)

greet("Harry")
 
#default parameter value "Stranger" will be used here. 
# Without default parameer value, this function will show error
greet()