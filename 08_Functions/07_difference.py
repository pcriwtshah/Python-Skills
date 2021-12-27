#This program will define a function to find the difference of two numbers.

#Defining the function
def diff(a,b):
    return a-b
x = int(input("Enter the first number\n"))
y = int(input("Enter the second number\n"))
print("The difference of",x, "and", y, "is", diff(x,y))