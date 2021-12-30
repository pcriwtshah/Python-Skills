#This program will define a function to find the product of two numbers.

#Defining the function
def product(a,b):
    return a*b
x = int(input("Enter the first number\n"))
y = int(input("Enter the second number\n"))
print("The product of",x, "and", y, "is", product(x,y))