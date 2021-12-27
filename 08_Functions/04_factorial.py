#This program will define a function to find the factorial of a number.

#Defining the function
def factorial(x):
    a = 1
    for i in range(1, x+1):
        a = a * i
    return a

#Using the function
num = int(input("Enter the number\n"))
if num == 0:
    print("The factorial of", num, "! is 1.")
elif num > 0:
    print("The factorial of", num, "! is", factorial(num))
else:
    print("The factorial is not defined for negative numbers")


