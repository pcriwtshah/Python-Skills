#This program creates a function to find the square of a number

#This program works
def sq(x):
    x = x*x
    return x
num = int(input("Enter the number\n"))
print("The square of", num, "is", sq(num))

'''
Q1. If num is int, how to find the square of a decimal number?
Q2. If num is float, how to find the sqaure of a negative number?
Think about data type "Long"
'''