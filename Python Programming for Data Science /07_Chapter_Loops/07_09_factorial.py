#This program will calculate the factorial of a given number.
# n! = (1)(2)(3)(4)........(n-2)(n-1)n
# 5! = 1*2*3*4*5
num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i

print(f"The factorial of {num} is {factorial}")
