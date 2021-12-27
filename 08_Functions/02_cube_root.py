# This program defines a function to find the cube root and 
# finds the cube root using the function

#Defining the function
def curt(number):
    b=0
    while b*b*b <= number:
        c = b
        b +=0.001
    return round(c,3)

#Finding the square root using the function
num = int(input("Enter the number\n"))
if num < 0:
    print("The cube root of a negative number is undefined in a real number system")
else:
    print("The cube root of ",num,"is",curt(num))

