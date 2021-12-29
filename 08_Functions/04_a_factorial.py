#This program will define a function to find the factorial of a number and 
# use the function to calculate the factorial.

#Defining the function
def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

 #Using the function   
num = int(input("Enter the number"))
print(f"The factorial of {num} is {factorial(num)}")
