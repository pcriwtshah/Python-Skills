#This program will define a function to find the sum of two numbers.

#Defining the function
def sum(a,b):
    return a+b

#Using the function
x = int(input("Enter the first number\n"))
y = int(input("Enter the second number\n"))
print("The sum of",x, "and", y, "is", sum(x,y))