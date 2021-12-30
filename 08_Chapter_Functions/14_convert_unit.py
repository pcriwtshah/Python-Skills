#This program will define a function to convert celcius to farenheit 
#Defining the function
def faren(c):
    return (9/5)*c +32
#Using the function
c = float(input("Enter the temperature in Celsius\n"))
print(f"The {c} degree in Celsius is equal to {faren(c)} degree in Farenheit")


def celsius(f):
    return (5*(f - 32))/9
#Using the function
c = float(input("Enter the temperature in Farenheit\n"))
print(f"The {c} degree in Farenheit is equal to {celsius(c)} degree in Celsius")